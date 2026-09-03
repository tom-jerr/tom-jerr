# Hi there 👋

[![GitHub](https://img.shields.io/badge/GitHub-tom--jerr-181717?style=flat\&logo=github)](https://github.com/tom-jerr)
[![Zhihu](https://img.shields.io/badge/Zhihu-blue?style=flat\&logo=zhihu\&logoColor=white)](https://www.zhihu.com/people/chen-wen-de-jian-ke)
[![Gmail](https://img.shields.io/badge/Gmail-tomlzy213%40gmail.com-EA4335?style=flat\&logo=gmail\&logoColor=white)](mailto:tomlzy213@gmail.com)
[![Website](https://img.shields.io/badge/Website-tom--jerr.github.io-4285F4?style=flat\&logo=googlechrome\&logoColor=white)](https://tom-jerr.github.io/)

<img align="right" width="260" alt="bug cat" src="https://raw.githubusercontent.com/tom-jerr/MyblogImg/main/bug_cat.gif" />

## 👋 Hi, I'm Zhiyi Liu

🎓 Master's student in Computer Science at **University of Electronic Science and Technology of China (UESTC)**, graduating in **2027**.

⚡ I focus on **LLM inference acceleration, CUDA kernel optimization, and high-performance AI systems**.

💼 Currently working on **LLM inference optimization**, including low-bit quantization, KV Cache optimization, MoE serving, scheduling, and end-to-end performance profiling.

🔎 **Seeking 2027 New Grad opportunities (秋招)** in:

* **LLM Inference / Model Systems**
* **AI Infrastructure**
* **High-Performance ML Systems**

📫 **Contact:** [tomlzy213@gmail.com](mailto:tomlzy213@gmail.com)
🌐 **Blog:** [tom-jerr.github.io](https://tom-jerr.github.io/)

<br clear="right"/>

---

## 🔥 What I'm Working On

My current interests are centered around making large language models **faster, cheaper, and more scalable**:

* **LLM Serving:** SGLang, vLLM, continuous batching, chunked prefill, overlap scheduling
* **KV Cache:** Paged KV Cache, Radix / Prefix Cache, KV Cache quantization
* **Speculative Decoding:** EAGLE-style speculative inference and pipeline overlap
* **CUDA:** GEMM, Tensor Core MMA, FlashAttention, RMSNorm, Softmax, CUDA Graph
* **Distributed Inference:** TP / DP / EP, PD disaggregation, NCCL / RDMA communication

---

## 🚀 Featured Projects

### [MiniInfer](https://github.com/tom-jerr/MiniInfer)

A lightweight high-performance **LLM inference engine built from scratch**, designed to understand and reproduce the core techniques used by modern serving systems such as vLLM and SGLang.

**Implemented:**

* Paged KV Cache & Radix Prefix Cache
* Continuous Batching & Chunked Prefill
* CUDA Graph & Breakable CUDA Graph
* SGLang-style Overlap Scheduling
* FlashAttention2 & FlashInfer backends
* Multi-process Tokenizer / Scheduler / Detokenizer pipeline
* Qwen2 / Qwen3 / Qwen3-MoE inference
* FusedMoE and TP / EP-ready execution

On A100, the optimized engine reaches performance close to or above vLLM in several decode-heavy workloads.

---

### [cuda-learn](https://github.com/tom-jerr/cuda-learn)

A hands-on CUDA kernel optimization project with handwritten kernels exposed through **TVM FFI + PyTorch bindings**, together with correctness tests and reproducible benchmarks.

Implemented and studied:

* Vectorized memory access & memory coalescing
* Shared-memory tiling & bank-conflict optimization
* SGEMM
* BF16 Tensor Core MMA
* FlashAttention
* Softmax
* RMSNorm / Fused RMSNorm
* SiLU-and-Mul
* SGEMV
* Top-K
* Parallel Prefix Sum
* CUDA Graph
* CUDA Memory Pool & IPC

Benchmarks compare handwritten kernels directly against libraries such as **cuBLAS, cuDNN, and FlashAttention**.

---

### [SGLang](https://github.com/tom-jerr/sglang)

My main playground for studying and experimenting with production-grade LLM inference systems.

Areas I have worked with include:

* Chunked Prefill and mixed scheduling
* Breakable CUDA Graph
* Speculative decoding
* Prefix / Radix Cache

---

### [Nebula Graph — ANN Search](https://github.com/tom-jerr/nebula)

Added native **Approximate Nearest Neighbor (ANN) vector search** capabilities to a distributed graph database.

This project gave me hands-on experience with:

* Large C++ codebases
* Distributed storage systems
* Query execution
* Indexing and vector search
* Systems-level performance optimization

---

## 📚 Systems Background

Before focusing on LLM systems, I also worked on several systems projects:

* **TinyKV** — Distributed KV store with Raft and transaction support
* **BusTub** — Relational database components and SQL query execution
* **MapReduce (6.824)** — C++ / gRPC implementation of MapReduce
* **RelayServer** — High-performance network relay server based on `epoll`

These projects built the systems foundation that I now apply to **LLM serving and GPU infrastructure**.

---

## 📊 GitHub Stats

<p align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=tom-jerr&show_icons=true&hide_border=true" />
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=tom-jerr&layout=compact&hide_border=true" />
</p>

---

## 🌱 About Me

I'm interested in the intersection of **GPU architecture, ML systems, and distributed systems**.

I enjoy understanding an inference system all the way from:

**CUDA kernels → model execution → KV Cache → scheduler → distributed communication → end-to-end serving performance.**

My current goal is simple:

> **Make LLM inference faster, more memory-efficient, and more scalable.**
