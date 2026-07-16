# Before Class — L08 — Computer Vision

**Estimated time: ~30 minutes.** Complete this before class.

This is the simplest version of "show up prepared": watch a short intro, run one notebook, answer a few questions. You'll come to class having seen the idea in action.

| Step | Time | What you do |
|---|---|---|
| **0. Watch** | ~5 min  | Watch the [lesson intro video](https://youtu.be/jBGYGwABXeQ) |
| **1. Try it** | ~20 min | Open and run `notebooks/01_morning_briefing.ipynb` |
| **2. Reflect** | ~5 min  | Three short questions below |

---

## Step 0 — Watch the intro video (~5 min)

▶️ **[L08 How AI learn to see](https://youtu.be/jBGYGwABXeQ)**

A short orientation to the day: why images break the flattened-features approach from L07, and what Sarah is about to build for Marcus's product-photo auto-tagging request. Watch it before opening the notebook.

🕹️ **After the video:** open the [interactive key-concepts page](https://su-ntu-ctp.github.io/6m-data-3.8-Computer-Vision/) and play with it for 10–15 minutes. Drag the sliders, click the buttons — you can't break anything. Arriving in class having *seen* these ideas move makes the session far easier.

---

## Step 1 — Try it (~20 min)

Open **`notebooks/01_morning_briefing.ipynb`** in VS Code with the `dsai-m3` kernel. Run every cell top to bottom. Read the markdown between cells. Don't skip any cell.

Marcus's next ask: *"Can we auto-tag the 10,000 product photos uploaded each season?"* The notebook starts with Fashion-MNIST and shows what an MLP can do on flattened pixels (~87% accuracy, but lots of parameters). It then sets up the CNN motivation that you'll explore in class.

If this is your first time running a notebook in this repo, see [setup.md](./setup.md) once — you only need to do this for the first lesson.

---

## Step 2 — Quick reflection (~5 min)

Write a sentence or two for each. You can scribble in a notebook, in a journal, or just hold the answer in your head — what matters is that you *tried*.

**Q1. Why don't MLPs scale to real images?**

An MLP on 224×224 colour photos would need ~38 million parameters in the first layer alone. What's the alternative?

**Q2. Translation invariance.**

A cat is a cat whether it's in the top-left or bottom-right of the photo. How could you design a model that builds in that property?

**Q3. Transfer learning, intuitively.**

If you had 500 product photos to classify, would you train a model from scratch or start from one trained on 1.2M ImageNet photos? Why?

---

## Bring to class

- Your answer to Q3.
- One image-classification task from your own domain (medical, retail, satellite, …) where transfer learning would or wouldn't fit.

---

**Want to go deeper before class?** See **[reference.md](./reference.md) → *Further reading & watching*** at the bottom — videos and recommended readings that used to live in this guide.

**Ran out of time?** Doing just Step 1 (running the notebook) is enough. The class builds on having felt what the lesson teaches; the reflection questions get re-asked live.
