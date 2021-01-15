import streamlit as st
from SPARQLWrapper import SPARQLWrapper, JSON
from streamlit_agraph import agraph, TripleStore, Node, Edge, Config
import json

def get_inspired():
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    
    query_string = """
    SELECT ?name_pe1_en ?rel_en ?name_pe2_en
    WHERE {
      {
           SELECT ?name_p1 ?rel ?name_p2
           WHERE {
               ?p1 a foaf:Person .
               ?p1 dbo:influencedBy ?p2 .
               ?p2 a foaf:Person .
               ?p1 foaf:name ?name_p1 .
               ?p2 foaf:name ?name_p2 .
              dbo:influencedBy rdfs:label ?rel .
              }
           LIMIT 100
      }
      UNION
      {
           SELECT ?name_p1 ?rel ?name_p2
           WHERE {
              ?p1 a foaf:Person .
              ?p1 dbo:influenced ?p2 .
              ?p2 a foaf:Person .
              ?p1 foaf:name ?name_p1 .
              ?p2 foaf:name ?name_p2 .
              dbo:influenced rdfs:label ?rel .
          }
       LIMIT 100
      }
      FILTER ( LANG(?name_p1) = "en" && LANG(?rel) = "en" && LANG(?name_p2) = "en" )
      BIND ( STR(?name_p1) AS ?name_pe1_en )
      BIND ( STR(?rel) AS ?rel_en )
      BIND ( STR(?name_p2) AS ?name_pe2_en )
    }
    """
    
    sparql.setQuery(query_string)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    store = TripleStore()
    for result in results["results"]["bindings"]:
        node1 = result["name_pe1_en"]["value"]
        link = result["rel_en"]["value"]
        node2 = result["name_pe2_en"]["value"]
        store.add_triple(node1, link, node2)
    return store

def app():
    st.title("Graph Example")
    config = Config(height=600, width=700, nodeHighlightBehavior=True, highlightColor="#F7A7A6", directed=True,
                    collapsible=True)
    
    with st.spinner("Loading data"):
      store = get_inspired()
      st.write("Nodes loaded: " + str(len(store.getNodes())))
    st.success("Done")
    agraph(list(store.getNodes()), (store.getEdges() ), config)


if __name__ == '__main__':
    app()
