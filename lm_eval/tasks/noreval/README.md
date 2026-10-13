# 🇳🇴 NorEval 1.1

### Paper

* Title: `NorEval: A Norwegian Language Understanding and Generation Evaluation Benchmark`
* Abstract: [arxiv.org/abs/2504.07749](https://arxiv.org/abs/2504.07749)
* Homepage: [github.com/ltgoslo/noreval](https://github.com/ltgoslo/noreval/tree/main)

**Overview of the NorEval design.**  😼 denotes datasets used in [NorBench](https://aclanthology.org/2023.nodalida-1.61/), [NLEBench](https://aclanthology.org/2024.emnlp-main.317/), [ScandEval](https://aclanthology.org/2023.nodalida-1.20/), and [SEB](https://proceedings.neurips.cc/paper_files/paper/2024/file/4746bb91bd073ec7eef930d5775122ba-Paper-Datasets_and_Benchmarks_Track.pdf); 🚀 represents datasets that have not been used in the existing Norwegian benchmarks; and 😎 denotes our novel datasets introduced as part of NorEval. EN=English; BM=Norwegian Bokmål; NN=Norwegian Nynorsk.

NorEval is a multi-task Norwegian language understanding and generation evaluation benchmark that combines existing peer-reviewed datasets with new datasets manually created from scratch. NorEval covers diverse task categories: sentiment analysis, Norwegian language knowledge, Norwegian-specific \& world knowledge, machine reading comprehension, commonsense reasoning, machine translation, text summarization, instruction following, and truthfulness. Our main evaluation principles are:

- 🌐 **Linguistic diversity**: support for both of the official written standards of Norwegian: Bokmål and Nynorsk (the minority variant).
- 📊 **Task diversity**: coverage of various least addressed tasks for Norwegian. In particular, only three out of 24 NorEval datasets are included in existing Norwegian benchmarks to date: [NorBench](https://aclanthology.org/2023.nodalida-1.61/), [NLEBench](https://aclanthology.org/2024.emnlp-main.317/), [ScandEval](https://aclanthology.org/2023.nodalida-1.20/), and [SEB](https://proceedings.neurips.cc/paper_files/paper/2024/file/4746bb91bd073ec7eef930d5775122ba-Paper-Datasets_and_Benchmarks_Track.pdf).
- 🧠 **Data quality**: focus on only peer-reviewed human-created datasets to ensure reliable evaluation in the context of the Norwegian language, culture, and values.
- 📏 **Prompt sensitivity**: evaluation across multiple human-written prompts to account for the prompt sensitivity.
- 👩🏻‍🔬 **Standardized evaluation**: integration of NorEval into LM Evaluation Harness for flexible and reproducible evaluation.

_____

### Tasks

|Name  |Bokmål | Nynorsk  | Northern Sámi | Task formulation  | Task category |
|:---|:---|:---|:---|:---|:---|
|[NoReC Sentence](https://huggingface.co/datasets/ltg/norec_sentence) |`norec_sentence`  | — | — |Text classification| Language understanding |
|[NoReC Document](https://huggingface.co/datasets/ltg/norec_document) |`norec_document`  | — | — |Text classification| Language understanding |
|[SLIDE](https://huggingface.co/datasets/ltg/slide) |`slide`  | `slide` | — |Text classification| Linguistic knowledge |
|[NCB](https://huggingface.co/datasets/hcfa/ncb) |`ncb`| — | — |Text classification| Linguistic knowledge   |
|[NoCoLA](https://huggingface.co/datasets/ltg/nocola) |`nocola`| — | — |Text classification| Linguistic knowledge   |
|[MultiBLiMP](https://huggingface.co/datasets/jumelet/multiblimp) | — | — |`noreval_multiblimp`|Text classification| Linguistic knowledge |
|[NorIdiom](https://huggingface.co/datasets/Sprakbanken/Norwegian_idioms) |`noridiom_nob`  | `noridiom_nno`  | — |Text classification| Linguistic knowledge |
|[NorBelebele](https://huggingface.co/datasets/ltg/norbelebele) |`norbelebele`| —| — |Text classification| Language understanding |
|[NRK-Quiz-QA](https://huggingface.co/datasets/ltg/nrk_quiz_qa) |`nrk_quiz_qa_nob`| `nrk_quiz_qa_nno`| — |Text classification| World knowledge and reasoning |
|[NorOpenBookQA](https://huggingface.co/datasets/ltg/noropenbookqa) |`noropenbookqa_nob`| `noropenbookqa_nno` | — |Text classification| Language understanding |
|[NorOpenBookQA (without facts)](https://huggingface.co/datasets/ltg/noropenbookqa) |`noropenbookqa_no_fact_nob`| `noropenbookqa_no_fact_nno` | — |Text classification| World knowledge and reasoning |
|[NorCommonsenseQA](https://huggingface.co/datasets/ltg/norcommonsenseqa) |`norcommonsenseqa_nob`| `norcommonsenseqa_nno` | — |Text classification|World knowledge and reasoning  |
|[NorTruthfulQA Multiple choice](https://huggingface.co/datasets/ltg/nortruthfulqa_mc) |`nortruthfulqa_mc_nob`| `nortruthfulqa_mc_nno` | — |Text classification | World knowledge and reasoning |
|[NorTruthfulQA Generation](https://huggingface.co/datasets/ltg/nortruthfulqa_gen) |`nortruthfulqa_gen_nob`| `nortruthfulqa_gen_nno` | — | Text generation|World knowledge and reasoning |
|[NorQuAD](https://huggingface.co/datasets/ltg/norquad) |`norquad`| —  | — |Text generation| Language understanding |
|[ASK-GEC](https://huggingface.co/datasets/ltg/ask-gec) |`ask_gec`| — | — |Text generation| Linguistic knowledge |
|[NorSumm](https://huggingface.co/datasets/SamiaT/NorSumm)  |`norsumm_nob` | `norsumm_nno`  | — |Text generation| Generation and summarization |
|[NorSumm Translation (Bokmål ↔ Nynorsk)](https://huggingface.co/datasets/ltg/norsumm-nob-nno-translation) | `norsumm_nob_nno_translation`| `norsumm_nno_nob_translation`  | — |Text generation|Generation and summarization |
|[Tatoeba (English → Bokmål/Nynorsk)](https://huggingface.co/datasets/Helsinki-NLP/tatoeba_mt) | `tatoeba_eng_nob`| `tatoeba_eng_nno`  | — |Text generation|Machine translation |
|[Tatoeba (Bokmål/Nynorsk → English)](https://huggingface.co/datasets/Helsinki-NLP/tatoeba_mt) | `tatoeba_nob_eng`| `tatoeba_nno_eng`  | — |Text generation|Machine translation |
|[Tatoeba (Bokmål ↔ Northern Sámi)](https://huggingface.co/datasets/ltg/saami-tatoeba) | `tatoeba_sme_nob` | — | `tatoeba_nob_sme`|Text generation|Machine translation |
|[NorRewrite-Instruct](https://huggingface.co/datasets/ltg/norrewrite-instruct) |`norrewrite_instruct`  | — | — |Text generation|Generation and summarization|
|[NorSummarize-Instruct](https://huggingface.co/datasets/ltg/norsummarize-instruct) |`norsummarize_instruct` | — | — |Text generation|Generation and summarization|

<details>
<summary><b>Table description</b></summary>

* **Name**: a dataset name with a HuggingFace link.
* **Bokmål**: the LM Evaluation Harness task name for the Norwegian Bokmål dataset. `slide`, which covers Bokmål, Nynorsk, Danish, and Swedish, is also listed here.
* **Nynorsk**: the LM Evaluation Harness task name for the Norwegian Nynorsk dataset, if available.
* **Northern Sámi**: the LM Evaluation Harness task name for the Northern Sámi dataset, if available. Translation tasks between Bokmål and Northern Sámi are listed here.
* **Task type**: the task type.
* **Task category**: the task category.

</details>

##### Comments on Belebele

Belebele for Norwegian Bokmål is already available in LM Evaluation Harness as `belebele_nob_Latn`. However, our version (`norbelebele`) supports five prompt templates written by Norwegian native speakers, which are different from the default prompt template used in Belebele. Our version is also based on the corrected Bokmål passages from FLORES+ -- [ltg/norbelebele](https://huggingface.co/datasets/ltg/norbelebele).

##### Comments on MultiBLiMP

MultiBLiMP is already available in LM Evaluation Harness as `multiblimp`. However, our evaluation focuses on Northern Sámi, and we evaluate each linguistic feature separately to get more informative results (unlike the official `lm-eval` MultiBLiMP).


### Changelog

**NorEval v1.1 (main branch)**
- New metadata: Every task now explicitly declares the primary metric, random-baseline performance, category and language(s). The order of metrics is changed to list the primary metric first.
- New task: [SLIDE](https://huggingface.co/datasets/ltg/slide) is a language identification task with five choices: Bokmål, Nynorsk, Danish, Swedish, or other language. One sentence can be compatible with multiple languages, a prediction is considered correct if it matches any of them.
- New task: [NoCoLA](https://huggingface.co/datasets/ltg/nocola), BLiMP-like Norwegian linguistic acceptability task.
- New task: Northern Sámi [MultiBLiMP](https://huggingface.co/datasets/jumelet/multiblimp) is actually a group of tasks, we evaluate each linguistic feature separately to get more informative results (unlike the official `lm-eval` MultiBLiMP).
- New task: NorOpenBookQA without facts is a simple rephrasing of the original NorOpenBookQA so that it evaluates knowledge rather then reading comprehension.
- New task: Bokmål ↔ Nynorsk translation based on the [NorSumm dataset](https://huggingface.co/datasets/SamiaT/NorSumm), which contains multi-sentence manual translations.
- New task: Bokmål ↔ Northern Sámi translation based on [ltg/saami-tatoeba](https://huggingface.co/datasets/ltg/saami-tatoeba).
- NorBelebele is now based on the corrected Bokmål passages from FLORES+ -- [ltg/norbelebele](https://huggingface.co/datasets/ltg/norbelebele).
- NorBelebele has two additional prompts, so that it's also evaluated in cloze formulation.
- ASK-GEC is now scored inside the harness, not in an extra post-production step.
- NorIdiom gets a new primary metric `em_first` and a less aggressive stopping criterion.
- The references in NorSumm are cleaned -- we strip newlines from the reference summaries, which broke few-shot evaluation previously.
- Hard-coded `num_fewshot: 0` are removed from `ncb`, `noridiom`, `norsumm`, `nortruthfulqa_gen`, `nortruthfulqa_mc` and `nrk_quiz_qa`.
- `num_beams: 1` is removed from all generative tasks, which previously broke evaluation with vLLM.
- `nortruthfulqa_gen`'s `doc_to_target` is changed from " " to `best_answer`, to work properly with few-shot evaluation.


### Citation

```
@article{mikhailov2025noreval,
  title={NorEval: A Norwegian Language Understanding and Generation Evaluation Benchmark},
  author={Mikhailov, Vladislav and Enstad, Tita and Samuel, David and Farseth{\aa}s, Hans Christian and Kutuzov, Andrey and Velldal, Erik and {\O}vrelid, Lilja},
  journal={arXiv preprint arXiv:2504.07749},
  year={2025}
}
```

### Checklist

* [x] Is the task an existing benchmark in the literature?
  * [x] Have you referenced the original paper that introduced the task?
  * [ ] If yes, does the original paper provide a reference implementation?
    * [ ] Yes, original implementation contributed by author of the benchmark

If other tasks on this dataset are already supported:
* [x] Is the "Main" variant of this task clearly denoted?
* [x] Have you provided a short sentence in a README on what each new variant adds / evaluates?
* [ ] Have you noted which, if any, published evaluation setups are matched by this variant?
