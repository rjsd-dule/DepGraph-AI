# DepGraph-AI

DepGraph-AI is a tool that automatically analyzes dependencies between Python code files and generates intelligent documentation using language models (LLMs). It is ideal for refactoring, onboarding new developers, or detecting fragile code. Currently, as a development version, it is focused solely on reviewing code with the .py extension.

- Uses AI to explain functions.
- Identifies internal and external dependencies.
- Generates automatic relationship graphs.
- Exports results in JSON for further analysis.

---

## Part of the Project Structure

```
DepGraph-AI/
├── analyserCode/               # Folder with the code files to be analyzed
├── LLM_model/
│   └── run_analysis.py         # Runs the analysis with an LLM model
├── patrones.py                 # Defines patterns to look for in the code
├── alldef.py                   # Helper functions to process files
├── outputConsole.py            # Displays enhanced results in the console
├── guardar_resultados.py       # Saves results to a JSON file
├── graph.py                    # Generates a visual graph with NetworkX
├── main.py                     # Entry point of the application
├── resultados/                 # Output for individual files
├── resultados_dependencias/    # General output of analysis and graph
└── requirements.txt            # Python environment requirements
```

---

## Instalación y Requisitos

Requiere **Python 3.8+**. To install all the necessary dependencies:

```bash
pip install -r requirements.txt
```

### Dependencias utilizadas:

#### Analysis and Visualization:
- **networkx** – for building the graph of internal dependencies between files.
- **matplotlib** – for displaying and saving the graph as an image (.png).

#### Language Models (LLMs with Gemini/Google AI):
- **langchain-core==0.3.55** – core for orchestrating process chains.
- **langchain==0.1.20** –  full version of LangChain with utilities and abstractions.
- **langchain-google-genai==2.1.3** – LangChain integration with Gemini (Google Generative AI).
- **google-generativeai==0.8.5** – official client for using Gemini directly from Python.
- **google-ai-generativelanguage==0.6.16** –  base APIs from Google AI for language models.

These libraries allow for analyzing source code functions using AI to generate automatic explanations.

---

## How to Run It

1. Place the `.py` files you want to analyze inside the `analyserCode/` folder.
2. Run the analysis:

```bash
python main.py
```

3. The program:
   - Analyzes all imports between files.
   - Separates internal dependencies (within the project) from external dependencies (libraries).
   - Generates a `dependencias.json` file.
   - Displays a graph of internal dependencies.
   - Uses an LLM model to explain the functions found.

---

## Dependency Graph View

> Code dependency graph.

![Grafo de dependencias](img/graficaIA.png)

---

## LLM Analysis View

> Sample of the file analysis by the LLM model. The code analysis process begins when the graph is closed. Once the analysis is completed, the result is saved in an .md file at the root of the project, named finalanalysis.md

![Ejemplo de análisis con LLM](img/model_outPut.png)

---

## Exported Results

- `resultados/[archivo].json` → individual results.
- `resultados_dependencias/dependencias.json` → general summary.
- Dependency visualization with NetworkX and Matplotlib.

---

## Customization

- Modify `patrones.py` to add new analysis rules without implementation.
- Customize the behavior of the language model from `LLM_model/run_analysis.py`.
