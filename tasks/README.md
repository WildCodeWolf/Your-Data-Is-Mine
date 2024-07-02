This directory contains tasks in form of short text files that
contain the tasks' description and goals as well as the owner.
The naming convention enables a Kanban-like approach to working
with those files. The details are explained below.

# Naming Convention

Task notes should be named and renamed following this pattern:

    `<status>.<task>.<priority>.md`

`<status>` is one of those options:

    open    : no owners, no progress made yet
    wip     : Work In Progress; has a dedicated task owner, report is expected
    done    : finished/ accomplished task
    topic   : not an actionable itself, but an area or topic that produces
              actionable tasks; however, should have a concrete goal just as well
              (primarily for brainstorming or outlining)

`<task>` should contain the key expression for the task, to grasp
at a glance what's in the note while the file content describes
the details. Use dash (`-`) or underscore (`_`) instead of whitespace (` `).

`<priority>` is a number between 1 and 5 with the meaning as follows:

    1 - TOP         : requires immediate action
    2 - IMPORTANT   : should be processed ASAP (e.g. other tasks depend on it)
    3 - NORMAL      : important to reach milestone, but can be delayed
    4 - LOW         : contributes to milestone, but probably has lesser impact
    5 - OPTIONAL    : optional feature or idea to improve overall performance/
                      output, but can be dropped entirely without consequences

## Examples

`done.firewall-eda.3.md`<br/>
`open.phishing-cnn.3.md`<br/>
`topic.presentation.2.md`<br/>
`topic.presentation-style.2.md`<br/>
`wip.phishing-random-forest.3.md`<br/>

# Content (Template)

Each note must contain the following sections: `Description`, `Goal` and
`Owner`. Following is a template of such a file:

    # Description

    ---

    # Goal

    ---

    # Owner

The `Description` should summarize the task and potentially point out
obstacles or resources to consider.
The `Goal` must be a clearly defined condition that qualifies the task
as completed once met. Avoid ambigous or subjective formulations here.
The `Owner` is the person who claimed the task, that is, who changed its
state from `open` to `wip`. This person is then responsible for seeing
it to its completed state.

# Workload

We aggreed on having *at most two* tasks per collaborator in `wip` stage.
The maximum number of concurrent `wip` notes is thus *eight*.

# Moderation of this Directory

We have not (yet) agreed on a moderator/ manager of the `tasks/`
directory.
