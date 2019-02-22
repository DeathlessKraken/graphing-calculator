# graphing-calculator
A graphing calculator made with TkInter, numpy, matplotlib, etc.

## Project Status:
### Unreleased
So far, I am able to display a custom plot from MatPlotLib in a TkInter frame. I managed to implement the standard toolbar for analyzing the graph in detail. There is also a quit button that functions successfully.

## Next Steps: Live graph from user input


## Problems I've had:
1) Delivery. Local app, or web app?
		I was caught up in how my project should look, when I realized I should only care about core functionality for now.
		I just need to get started, create a base, and go from there. It's good to think about future scalability, but only to a certain point.
		It won't matter if you're thinking about the future so much that you forget to start the project.
    Learning entire frameworks for little ROI is not an efficient use of my time. I can learn it, but right now there is no need to.

2) So far I've managed to display a matplotlib graph with its toolbar, a quit button, and a label. The toolbar for the graph is separate from it's graph.
	Every other implementation has the toolbar left justified; why is mine centered? I don't like that. How can I center it?

	Got it! I had to add "sticky='w'" to the grid method in the Graph frame class, after creating the widgets. I solved this problem by messing around in key areas of my code
 
## Sources: 
