---
name: networkx
description: Use when creating, analyzing, importing, exporting, or visualizing Python
  NetworkX graphs for relationship data, graph algorithms, shortest paths, centrality,
  clustering, communities, synthetic networks, topology, or knowledge graphs.
---

# NetworkX

## Local Metadata Notes

- Former frontmatter `metadata`: short-description=Analyze Python graphs with NetworkX

Use this skill for Python graph and network analysis. Preserve the upstream
intent: NetworkX is for building graph structures, computing graph algorithms,
loading/exporting graph data, and making network visualizations across domains
such as social networks, biology, transportation, citations, infrastructure,
knowledge graphs, and any pairwise relationship data.

Follow the project's dependency policy first. If NetworkX is missing, verify the
active package manager before installing anything.

## Use When

- Building graphs from edges, adjacency data, matrices, tables, JSON, GraphML, or
  other relationship data.
- Computing shortest paths, connectivity, centrality, PageRank, clustering,
  communities, flows, spanning trees, matching, coloring, or isomorphism.
- Generating synthetic networks for tests or simulations.
- Visualizing networks with matplotlib, Plotly, PyVis, GraphML/Gephi, or
  similar tooling.
- Debugging graph directionality, weights, disconnected components, attributes,
  node identifiers, or algorithm assumptions.

## Skip When

- The user wants to build a persistent knowledge graph from a document/code
  corpus; use `graphify`.
- The user wants a text-native explanatory diagram; use `markdown-mermaid-writing`.
- The task is a discrete-event simulation; use `simpy`.
- The task needs a production graph database query layer rather than in-process
  Python graph analysis.

## Workflow

1. Clarify graph semantics.
   - Directed or undirected?
   - Weighted or unweighted?
   - Single-edge or multi-edge?
   - Which fields are node IDs, edge attributes, and metadata?
2. Load or build the graph.
   - Pick `Graph`, `DiGraph`, `MultiGraph`, or `MultiDiGraph`.
   - Preserve node and edge attributes if they affect analysis.
3. Inspect structure before algorithms.
   - Count nodes/edges, density, components, isolates, degree distribution, and
     directedness.
4. Choose algorithms based on the question.
   - Confirm assumptions such as connectivity, nonnegative weights, DAG-only
     algorithms, or directed vs undirected behavior.
5. Validate results.
   - Sanity-check on a small subgraph or known example.
   - Set seeds for random graph generation and force-directed layouts.
   - For large graphs, consider approximate algorithms or sparse matrices.
6. Export results.
   - Save graph data and computed metrics in formats that preserve needed
     attributes.

## Core Pattern

```python
import networkx as nx
import pandas as pd

edges = pd.DataFrame(
    {
        "source": ["a", "a", "b", "c"],
        "target": ["b", "c", "d", "d"],
        "weight": [1.0, 2.0, 1.5, 0.5],
    }
)

G = nx.from_pandas_edgelist(
    edges,
    source="source",
    target="target",
    edge_attr="weight",
    create_using=nx.Graph(),
)

print(G.number_of_nodes(), G.number_of_edges())
print(nx.shortest_path(G, "a", "d", weight="weight"))
centrality = nx.betweenness_centrality(G, weight="weight")
```

## Graph Type Selection

| Need | Type |
| --- | --- |
| Undirected relationships with at most one edge per pair | `nx.Graph` |
| Direction matters, at most one edge per ordered pair | `nx.DiGraph` |
| Parallel undirected edges matter | `nx.MultiGraph` |
| Parallel directed edges matter | `nx.MultiDiGraph` |

Use explicit edge attributes for weight, capacity, cost, timestamp, relation, or
evidence. Do not overload node IDs with metadata that should be an attribute.

## Algorithm Selection

| Question | NetworkX family | Reference |
| --- | --- | --- |
| How connected is the graph? | components/connectivity | `references/algorithms.md` |
| What is the shortest or cheapest path? | shortest paths | `references/algorithms.md` |
| Which nodes are important? | centrality/PageRank | `references/algorithms.md` |
| Are there clusters or communities? | community detection | `references/algorithms.md` |
| How does flow move through edges? | max flow/min cut | `references/algorithms.md` |
| Are two graphs structurally equivalent? | isomorphism | `references/algorithms.md` |
| Need synthetic test graphs? | graph generators | `references/generators.md` |
| Need import/export formats? | graph I/O | `references/io.md` |
| Need a figure? | visualization/layouts | `references/visualization.md` |

## Bundled Resources

- `references/graph-basics.md`: graph types, attributes, subgraphs, and basic
  operations.
- `references/algorithms.md`: paths, centrality, clustering, communities, flow,
  trees, traversal, matching, coloring, and isomorphism.
- `references/generators.md`: classic, random, lattice, bipartite, and
  specialized graph generators.
- `references/io.md`: edge lists, adjacency lists, GraphML, GML, JSON, CSV,
  Pandas, NumPy, SciPy sparse arrays, databases, and format selection.
- `references/visualization.md`: layouts, drawing, labels, interactive
  visualizations, and publication-quality figures.

## Validation Checklist

- Graph direction, weights, and multiplicity match the real data.
- Node IDs are stable and hashable; metadata is stored as attributes.
- Algorithm assumptions are satisfied before calling the function.
- Random seeds are fixed for generated graphs and non-deterministic layouts.
- Large graph memory and runtime costs are considered.
- Results are checked on a tiny example or known subgraph.
- Exports preserve the attributes needed by downstream tools.

## Common Pitfalls

- Running undirected algorithms on a directed graph without deciding semantics.
- Forgetting the `weight` parameter when edge weights matter.
- Assuming all graphs are connected.
- Treating layout coordinates as analytical evidence.
- Losing attributes when exporting to a simpler format.
- Using exact expensive algorithms on graphs large enough to need approximation.

## Related Skills

- Use `graphify` for building and querying a persistent corpus-derived knowledge
  graph; use this skill for custom Python graph algorithms and analysis.
- Use `simpy` when graph topology is only one part of a discrete-event model.
- Use `markdown-mermaid-writing` to document a small graph, topology, or
  algorithm flow in Markdown.

## Attribution

Adapted for Codex from the K-Dense `scientific-agent-skills` NetworkX skill
under its 3-clause BSD license.
