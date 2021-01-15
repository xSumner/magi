import streamlit
from streamlit_agraph import agraph, Node, Edge, Config

nodes = []
edges = []
nodes.append( Node(id="蜘蛛侠", label="蜘蛛侠", size=400, svg="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_spiderman.png") ) # includes **kwargs
nodes.append( Node(id="惊奇队长", size=400, svg="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_captainmarvel.png") )
nodes.append( Node(id="钢铁侠", size=400, svg="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_ironman.png") )
edges.append( Edge(source="惊奇队长", label="朋友", target="蜘蛛侠", type="CURVE_SMOOTH") ) # includes **kwargs
edges.append( Edge(source="钢铁侠", label="师徒", target="蜘蛛侠", type="CURVE_SMOOTH") )

config = Config(width=800, 
                height=800, 
                directed=False,
                nodeHighlightBehavior=True, 
                highlightColor="#F7A7A6", # or "blue"
                collapsible=True,
                node={'labelProperty':'label'},
                link={'labelProperty': 'label', 'renderLabel': True}
                # **kwargs e.g. node_size=1000 or node_color="blue"
                ) 

return_value = agraph(nodes=nodes, 
                      edges=edges, 
                      config=config)