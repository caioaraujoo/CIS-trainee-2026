# Período 3 — Sistema RAG (Retrieval-Augmented Generation)

## Objetivo

Pipeline básico de RAG para responder perguntas com base em uma coleção de textos, integrando recuperação vetorial e geração de linguagem natural.

## Dataset

- **Fonte:** [IMDB Dataset (HuggingFace)](https://huggingface.co/datasets/scikit-learn/imdb)
- **Conteúdo:** reviews de filmes; amostra de 1.000 registros usada como base de contexto

## Ambiente

- **Python:** [3.14.5]
- **Libs principais:** `langchain`, `langchain-community`, `transformers`, `datasets`, `sentence-transformers`, `faiss-cpu`

## Pipeline

1. **Indexação** — textos divididos em chunks (`RecursiveCharacterTextSplitter`) e armazenados em índice vetorial `FAISS`, com embeddings do `all-MiniLM-L6-v2`.
2. **LLM** — `gpt2` via `pipeline` da Hugging Face, encapsulado no formato LangChain.
3. **Orquestração** — chain `RetrievalQA` conectando pergunta → busca no índice → geração da resposta.

## Como rodar

```bash
pip install -r requirements.txt
```

1. Não é necessário baixar dados manualmente — o download é automático via `datasets`.
2. Rode o notebook célula a célula para indexar a base e executar a inferência.

## Observações

- O modelo `gpt2` foi escolhido por ser leve e executável localmente, atendendo ao propósito didático do projeto. Por ser um modelo mais antigo e de menor porte, a qualidade das respostas geradas é limitada.
- O processamento foi restrito a 1.000 registros para viabilizar uma indexação rápida do FAISS em ambiente de CPU.
- Este período apresentou desafios significativos de implementação: o volume de conceitos novos (recuperação vetorial, embeddings, orquestração de chains) precisou ser assimilado em um prazo curto, o que impactou diretamente a etapa prática do desenvolvimento.
