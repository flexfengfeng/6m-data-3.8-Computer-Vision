# Setup — L08 — Computer Vision & CNNs

> One-time environment setup. **If you already set up the `dsai-m3` environment for L01–L07, you're almost done — L08 needs `torch >= 2.2` and `torchvision >= 0.17`. If you created the environment from any lesson's `environment.yml`, both are already included; otherwise run `pip install torch torchvision` once inside the activated environment. Then just clone this repo and pick the `dsai-m3` kernel.**

This guide gets you from "fresh machine" to "running the L08 notebooks". It takes about 15 minutes the first time.

---

## 1. Prerequisites

You need:

- **Git** — to clone this repository
- **Miniconda** (or Anaconda) — to create the Python environment. [Install Miniconda →](https://docs.conda.io/projects/miniconda/en/latest/)
- **VS Code** — with the Python and Jupyter extensions. [Download VS Code →](https://code.visualstudio.com/)

Check git and conda are working:

```bash
git --version
conda --version
```

---

## 2. Clone this repository

```bash
git clone https://github.com/su-ntu-ctp/6m-data-3.8-Computer-Vision.git
cd 6m-data-3.8-Computer-Vision
```

---

## 3. Create the conda environment

From inside the `6m-data-3.8-Computer-Vision` folder:

```bash
conda env create -f environment.yml
```

This creates an environment called **`dsai-m3`** with Python, pandas, numpy, matplotlib, scikit-learn, PyTorch + torchvision, and Jupyter. It takes 5–10 minutes (torch is a large download).

> **Already have a `dsai-m3` environment from L01–L07?** You don't need to recreate it. Just confirm torch and torchvision are present:
>
> ```bash
> conda activate dsai-m3
> python -c "import torch, torchvision; print(torch.__version__, torchvision.__version__)"
> ```
>
> If that errors, run `pip install "torch>=2.2" "torchvision>=0.17"` once.

Activate the environment:

```bash
conda activate dsai-m3
```

---

## 4. First-run downloads (automatic)

- **Datasets:** Fashion-MNIST (~30 MB) and CIFAR-10 (~170 MB) auto-download on first run via `torchvision.datasets`. They are gitignored, so they never bloat the repo. First download takes 1–3 minutes.
- **Models:** the transfer-learning notebooks download `resnet18` ImageNet weights (~45 MB) and optionally `mobilenet_v3_small` (~10 MB), cached in `~/.cache/torch/hub/`.

> **No GPU?** L08 runs end-to-end on CPU (~30 min for the CIFAR-10 + ResNet18 fine-tune), but on a free Colab T4 GPU it's ~2 min. Notebooks 03, 04, the assignment, and the extensions each have an **Open in Colab** badge at the top — click it, then **Runtime → Change runtime type → T4 GPU**.

---

## 5. Open the project in VS Code

```bash
code .
```

When VS Code opens, it may prompt you to install recommended extensions (Python, Jupyter). Accept.

---

## 6. Select the `dsai-m3` kernel

1. Open `notebooks/01_morning_briefing.ipynb`.
2. In the top-right of the notebook, click **Select Kernel**.
3. Choose **Python Environments → dsai-m3**.

If `dsai-m3` doesn't appear, restart VS Code and try again. If it still doesn't appear, run `conda env list` in a terminal to confirm the environment exists.

---

## 7. Smoke test

In `01_morning_briefing.ipynb`, run the first cell (the imports). If it completes without errors, you're set.

If you see `ModuleNotFoundError`, the wrong kernel is selected — go back to Step 6. If only `torch`/`torchvision` is missing, see Step 3's note.

---

## Troubleshooting

**`conda: command not found`** → Miniconda isn't installed or isn't on your PATH. Reinstall Miniconda and restart your terminal.

**`environment.yml` solver hangs** → Try `conda env create -f environment.yml --solver=libmamba`. If that still hangs, delete the env (`conda env remove -n dsai-m3`) and retry.

**Kernel doesn't appear in VS Code** → Run `python -m ipykernel install --user --name dsai-m3` from inside the activated environment.

**Dataset download fails mid-run** → Delete the partial `data/` download folder the cell created and re-run the cell.

---

Once setup is done, head back to **[README.md](./README.md)** → Phase 1.
