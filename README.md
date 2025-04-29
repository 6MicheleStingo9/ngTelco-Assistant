# ngTelco-Assistant

> Proof of Concept di assistente virtuale full-stack, sviluppato in Python, **LangChain-powered**, con logica avanzata di Retrieval-Augmented Generation (**RAG**).

## Introduzione

`ngTelco-Assistant` esplora la creazione di un **agente RAG** capace di recuperare informazioni da **tre fonti distinte**:

- **Database a grafo** (es. Neo4j) per dati strutturati e relazionali
- **Vector Store** (es. Qdrant, FAISS, Chroma, ecc.) per il recupero semantico di documenti
- **Mock API esterna** per simulare l'integrazione con servizi di terze parti

Questa architettura dimostra la flessibilità e la potenza di LangChain nell'orchestrare più fonti di conoscenza per arricchire il ragionamento dell'agente.

## Architettura del progetto

- `agent.py` → Definizione della logica dell'agente multi-retrieval
- `bot.py` → Avvio e gestione del bot
- `graph.py` → Interazione con il database a grafo
- `tools/` → Set di tool custom (es. retriever, API connector)
- `models/` → Modelli dati strutturati
- `data/` → Dataset di esempio
- `images/` → Risorse grafiche

## Requisiti

- Python 3.10+
- LangChain
- Neo4j (per il grafo)
- Qdrant o altro vector store

Installa tutto con:

```bash
pip install -r requirements.txt
```

## Esecuzione

Per avviare il bot:

```bash
streamlit run bot.py
```

## Stato del progetto

🛠️ Proof of Concept  
🌐 Dimostra integrazione avanzata di Knowledge Sources

## Licenza

Distribuito sotto licenza **MIT**.
