# graphing-calculator
A graphing calculator made with TkInter, numpy, matplotlib, etc.

## Project Status:
### Unreleased
So far, I am able to display a custom plot from MatPlotLib in a TkInter frame. I managed to implement the standard toolbar for analyzing the graph in detail. There is also a quit button that functions successfully.

## Next Steps: Live graph from user input


## Problems I've had:
### 1) Delivery. Local app, or web app?
I spent probably too much time thinking about how the final product should look. I knew I would most likely use TkInter for a desktop application, and MatPlotLib would generate some of the core functionality for the app. I considered that making a web application would be more convienient for showcasing the project and would be easier for anyone to access. I tried to plan out how I could deliver the web app; should I use Flask (which I already have experience in), Javascript, and rent a VPS? While it would give me more "experience" as a programmer, I would be spending way more time AND money than I would need to, just for appearances of the project. I don't want to be a web developer. I fell head over heels for the backend.

I was caught up in how my project should look, when I realized I should only care about core functionality for now.
I just need to get started, create a base, and go from there. It's good to think about future scalability, but only to a certain point.
It won't matter if you're thinking about the future so much that you forget to start the project.
Learning entire frameworks for little ROI is not an efficient use of my time. I can learn it, but right now there is no need to.

### 2) So far I've managed to display a matplotlib graph with its toolbar, a quit button, and a label. The toolbar for the graph is implemented separately.
Every other implementation has the toolbar left justified; why is mine centered? I don't like that. How can I center it?

Got it! I had to add "sticky='w'" to the grid method in the Graph frame class, after creating the widgets. I solved this problem by messing around in key areas of my code
 
## Sources: 

#### Websites
[MatPlotLib User's Guide](https://matplotlib.org/users/index.html)

[MatPlotLib Source Code](https://github.com/matplotlib/matplotlib)

[TkDocs](https://tkdocs.com/tutorial/index.html)

[Python.org TkInter Documentation](https://docs.python.org/3/library/tkinter.html)

[TkInter wiki](https://wiki.python.org/moin/TkInter)


#### Youtube
[Matplotlib Tutorial 16 - Live graphs](https://www.youtube.com/watch?v=ZmYPzESC5YY)

[How to Program a GUI Application (with Python Tkinter)](https://www.youtube.com/watch?v=D8-snVfekto)

