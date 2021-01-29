import streamlit as st
from streamlit_agraph import agraph, TripleStore, Node, Edge, Config
import json

# 应用标题
st.title("漫威英雄关系图谱")
# 定义图谱显示范围
config = Config(height=600, width=700, nodeHighlightBehavior=True, highlightColor="#F7A7A6", directed=True, collapsible=True)

# 读取数据并进行展示
with open("./marvel.json", encoding="utf8") as f:
  marvel_file = json.loads(f.read())
  marvel_store = TripleStore()
  for sub_graph in marvel_file["children"]:
    marvel_store.add_triple(marvel_file["name"], "has_subgroup", sub_graph["name"], picture=marvel_file["img"])
    for node in sub_graph["children"]:
      node1 = node["hero"]
      link = "blongs_to"
      node2 = sub_graph["name"]
      pic = node["img"]
      marvel_store.add_triple(node1, link, node2, picture=pic)
  agraph(list(marvel_store.getNodes()), (marvel_store.getEdges()), config)