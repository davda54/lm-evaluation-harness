from __future__ import annotations

import logging
from random import Random
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from collections.abc import Iterable, Sequence
    from typing import Any, TypeVar

    _T = TypeVar("_T")

eval_logger = logging.getLogger(__name__)


class ContextSampler:
    def __init__(
        self,
        df: Sequence[dict[str, Any]] | None = None,
        *,
        rnd: int | None = None,
        fewshot_indices: list[int] | None = None,
        **kwargs,
    ) -> None:
        self.rnd = Random(rnd)
        self.df = df or []
        self.fewshot_indices = fewshot_indices
        self._loaded = False  # to iterate over fewshot_indices when needed

    def sample(
        self,
        n: int,
        eval_doc: dict[str, Any] | None = None,
        df: Sequence[dict[str, Any]] | None = None,
        **kwargs,
    ) -> Sequence[dict[str, Any]]:
        """
        Sample n documents from the pool.

        Args:
            n: Number of documents to sample
            eval_doc: Optional document to exclude from sampling
            df: Optional list of documents to sample from

        Returns:
            List of sampled documents
        """
        assert n >= 0, "Error: number of samples requested must be >=0"
        if n == 0:
            return []

        if df:
            self.df = df

        assert self.df, "Error: no documents available for sampling."
        res = (
            self.rnd.sample(self.fewshot_docs(), n)
            if not eval_doc
            else self.rm_eval_doc(
                eval_doc, self.rnd.sample(self.fewshot_docs(), n + 1), n
            )
        )
        assert len(res) == n, (
            f"Error: number of fewshot samples returned ({len(res)}) not equal to number requested ({n})."
        )
        return res

    def set_rnd(self, rnd: int | None):
        self.rnd = Random(rnd)
        return self

    def replace_df(self, df: Sequence[dict[str, Any]]):
        self.df = df
        self._loaded = False
        return self

    def fewshot_docs(self):
        """Return cached fewshot docs if available"""
        if self._loaded:
            return self.df
        if self.fewshot_indices and self.df and not self._loaded:
            self.df = [self.df[i] for i in self.fewshot_indices]
        self._loaded = True
        return list(self.df)

    @staticmethod
    def rm_eval_doc(doc: _T, _iter: Iterable[_T], n=None) -> Sequence[_T]:
        return (
            [x for x in _iter if x != doc]
            if n is None
            else [x for x in _iter if x != doc][:n]
        )


class FirstNSampler(ContextSampler):
    def sample(self, n: int, eval_doc=None, df=None, **kwargs):
        """
        Draw the first `n` samples in order from the specified split.
        Used for tasks with "canonical" ordered fewshot examples, such as MMLU and CMMLU.
        """
        assert n <= len(self.df), (
            f"Error: number of fewshot samples requested exceeds the {len(self.df)} that are available."
        )
        return self.df[:n]


class BalancedSampler(ContextSampler):
    def sample(self, n: int, eval_doc=None, df=None, **kwargs):
        """
        TODO: this should return approximately class-balanced samples from our fewshot examples.
        TODO: what order should they be in? maybe random?
        """

        raise NotImplementedError


class ManualSampler(ContextSampler):
    def sample(self, n: int, eval_doc=None, df=None, **kwargs):
        """ """
        raise NotImplementedError


MAX_K = 10


class LeaveOneOutSampler(ContextSampler):
    """Sampler for tasks where few-shot examples come from the same split
    being evaluated (no separate training split). Pre-selects a fixed set of
    k primary demonstrations plus k reserves, then swaps out the current
    eval instance when it collides with a primary demo.

    Caps k at MAX_K=10 to limit distributional leakage on small splits.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._primary: list[dict] | None = None
        self._reserves: list[dict] | None = None

    def set_rnd(self, rnd: int | None):
        super().set_rnd(rnd)
        self._primary = None
        self._reserves = None
        return self

    def _init_pools(self, n: int) -> None:
        pool = self.fewshot_docs()
        n = min(n, MAX_K, len(pool))
        take = min(2 * n, len(pool))
        selected = self.rnd.sample(pool, take)
        self._primary = selected[:n]
        self._reserves = selected[n:]

    def sample(
        self,
        n: int,
        eval_doc: dict | None = None,
        df=None,
        **kwargs,
    ) -> list[dict]:
        assert n >= 0, "Error: number of samples requested must be >=0"
        if n == 0:
            return []

        if df:
            self.df = df

        if n > MAX_K:
            eval_logger.warning(
                "LeaveOneOutSampler: requested n=%d clamped to MAX_K=%d", n, MAX_K
            )
            n = min(n, MAX_K)

        if self._primary is None:
            self._init_pools(n)

        if eval_doc is None or eval_doc not in self._primary:
            return list(self._primary[:n])

        # eval_doc is one of the primaries — swap it with a reserve
        result = [d for d in self._primary if d != eval_doc][:n]
        if len(result) < n:
            for reserve in self._reserves:
                if reserve != eval_doc and reserve not in result:
                    result.append(reserve)
                    if len(result) == n:
                        break
        if len(result) < n:
            # Fallback: scan full pool (near-impossible with 800+ rows)
            for doc in self.fewshot_docs():
                if doc != eval_doc and doc not in result:
                    result.append(doc)
                    if len(result) == n:
                        break

        return result


SAMPLER_REGISTRY: dict[str, type[ContextSampler]] = {
    "default": ContextSampler,
    "first_n": FirstNSampler,
    "loo": LeaveOneOutSampler,
}


def get_sampler(name: str):
    try:
        return SAMPLER_REGISTRY[name]
    except KeyError as e:
        raise KeyError(
            f"Attempted to use contextsampler '{name}', but no sampling strategy for this name found! Supported model names: {', '.join(SAMPLER_REGISTRY.keys())}"
        ) from e
