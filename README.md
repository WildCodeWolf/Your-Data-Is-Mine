# Your-Data-Is-Mine

This is a collaborative project created in the context of aquiring certifications
in the data landscape from the German educational institute Greenbootcamps
(https://greenbootcamps.com).

This is an ongoing project and, as of now, the notebooks on the main
branch are still being synthesized and polished.
They are by no means in a finished state.

## The Team

Our team consists of four people:

- Dustin Lischke (https://github.com/WildCodeWolf): Data Scientist
- Nilgün Yesil (https://github.com/nye86): Data Scientist
- Stefani Reimers (https://github.com/201steffi): Data Analyst
- Tanvi Goel (https://github.com/tanvigoel6): Data Analyst

Nobody of us has had prior experiences in the field of cyber security.
But given its relevance in the modern world and our motivation to
challenge ourselves, we took it up to put the knwoledge and skills
that we acquired in the past three months to the test.

And in the end, this project earned us all the certificates in our
respective fields.

## Project Structure

For this project, we chose two datasets from different areas of
cyber security: Credit Card Fraud and Network Intrusion.

If you want to look into individual notebooks, feel free to do so.
However, there is an intended reading order that aligns with our
work structure.

In order to follow that, you can start with the notebook on the
general EDA for the [credit card](credit-card-eda.ipynb) dataset.
You will find links at the top and the bottom of every notebook
that direct you to the previous and the next notebook as well as
back to this README.

In general, we followed a simple pattern for the two datasets:
Beginning with an EDA we looked into what we are dealing with
and set up structures subsets for the following machinie learning
part.
After testing, comparing and tuning a wide selection of prototypes,
ultimately combining the best into a combined model with the goal
of creating the best tool for any of the underlying jobs, we
critically evaluate their capabilities, limits and challenges.

This is the point we arrived at for our aforementioned presentation.
Moving forward, we attempt to improve the results further by
applying more sophisticated techniques and algorithms.
This process is still work in progress, and is at the moment undertaken
by just one of the team members in their spare time.
Thus, there is no fixed update schedule and additions happen as they come.

## The Data

The data originates from two different sources and can be freely
downloaded.
In order to avoid redundancy, an unnecessarily large repository and
possibly legal actions the datasets themselves are not integrated into the
repo.  Instead, the `.gitignore` file prevents the `data/` directory from
being tracked except for a [README](data/README.md) file that provides
you with the sources as well as an explanation as to how the data has
been prepared before being used in the notebooks.

## The Result

The [presentation](presentation/SecureSphere_Innovations.pdf) that's
been created for showcasing our findings after two
weeks of collaborative work can be found in this repo as a PDF.

On the main branch, you will find the notebooks that systematically
go through our working process.
However, since we didn't consider the presentation the end of our
findings, some of us decided to look deeper into the challenges and
possibilities left open at that point.
Thus, you may expect infrequent additions, modifications and experiments
(and, of course, occasionally corrections) now and in future.

## Python Modules

The notebooks in this repository make extensive use of popular Python
modules for data analysis and data science, such as [`pandas`](https://pandas.pydata.org),
[`scikit-learn`](https://scikit-learn.org/stable/)
and [`seaborn`](https://seaborn.pydata.org) for visualization (among others).

On top of that, to streamline our workflows and generate homogenous
illustrations, we wrote two small custom packages.

`presentation` (`presentation/__init__.py`) is responsible for configuring
`seaborn` and define the color scheme that we use for our graphics.

In `utils` we collect a few small files with specific settings and
auxiliaries for the individual datasets as well as evaluation utilities.

--------------------------------------------------------------------------------

## Side Note: Collaboration

For coordinating and structuring our work together in a constructive and
non-overlapping way for the period of collaboration, we utilized a very simple
Kanban-inspired approach.
But instead of visualizing the tasks on a board or utilizing an external tool,
we kept to a simple practice of file creation, claiming and renaming.

This allowed us to stay focused without needing to set up an unnecessary overhead
of apps or website configurations.

If you're interested, you can find the [guidelines](tasks/README.md) (and the actual
task files) in the `tasks` directory.
