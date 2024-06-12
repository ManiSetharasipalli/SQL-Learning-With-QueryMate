from flask import Blueprint, render_template
from .helpers import get_concept_data

pages = Blueprint('pages', __name__)


@pages.route("/sql-default")
def sql_default():
    concept_name = "SQL Home"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-default.html", question=question, answers=answers, exercise=exercises)


@pages.route("/sql-intro")
def sql_intro():
    concept_name = "SQL Intro"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-intro.html", question=question, answers=answers, exercise=exercises)


@pages.route("/sql-syntax")
def sql_syntax():
    concept_name = "SQL Syntax"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-syntax.html", question=question, answers=answers, exercise=exercises)


@pages.route("/sql-data-types")
def sql_data_types():
    concept_name = "SQL Data Types"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-data-types.html", question=question, answers=answers, exercise=exercises)


@pages.route("/sql-select")
def sql_select():
    concept_name = "SQL Select"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-select.html", question=question, answers=answers, exercise=exercises)


@pages.route("/sql-distinct")
def sql_distinct():
    concept_name = "SQL Distinct"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-distinct.html", question=question, answers=answers, exercise=exercises)


@pages.route("/sql-where")
def sql_where():
    concept_name = "SQL Where"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-where.html", question=question, answers=answers, exercise=exercises)


@pages.route("/sql-order-by")
def sql_order_by():
    concept_name = "SQL Order By"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-order-by.html", question=question, answers=answers, exercise=exercises)


@pages.route("/sql-and-or")
def sql_and_or():
    concept_name = "SQL And & Or"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-and-or.html", question=question, answers=answers, exercise=exercises)


@pages.route("/sql-not")
def sql_not():
    concept_name = "SQL Not"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-not.html", question=question, answers=answers, exercise=exercises)


@pages.route("/sql-like")
def sql_like():
    concept_name = "SQL Like"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-like.html", question=question, answers=answers, exercise=exercises)


@pages.route("/sql-limit")
def sql_limit():
    concept_name = "SQL Limit"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-limit.html", question=question, answers=answers, exercise=exercises)


@pages.route("/sql-in")
def sql_in():
    concept_name = "SQL In"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-in.html", question=question, answers=answers, exercise=exercises)


@pages.route("/sql-between")
def sql_between():
    concept_name = "SQL Between"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-between.html", question=question, answers=answers, exercise=exercises)


# Aggregate Functions
@pages.route("/sql-max-min")
def sql_max_min():
    concept_name = "SQL Max and Min"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-max-min.html", question=question, answers=answers, exercise=exercises)


@pages.route("/sql-count")
def sql_count():
    concept_name = "SQL Count"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-count.html", question=question, answers=answers, exercise=exercises)


@pages.route("/sql-sum")
def sql_sum():
    concept_name = "SQL Sum"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-sum.html", question=question, answers=answers, exercise=exercises)


@pages.route("/sql-avg")
def sql_avg():
    concept_name = "SQL Avg"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-avg.html", question=question, answers=answers, exercise=exercises)


# Grouping and Filtering Grouped Data
@pages.route("/sql-group-by")
def sql_group_by():
    concept_name = "SQL Group By"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-group-by.html", question=question, answers=answers, exercise=exercises)


@pages.route("/sql-having")
def sql_having():
    concept_name = "SQL Having"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-having.html", question=question, answers=answers, exercise=exercises)


# Data Manipulation
@pages.route("/sql-insert-into")
def sql_insert_into():
    concept_name = "SQL Insert Into"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-insert-into.html", question=question, answers=answers, exercise=exercises)


@pages.route("/sql-update")
def sql_update():
    concept_name = "SQL Update"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-update.html", question=question, answers=answers, exercise=exercises)


@pages.route("/sql-delete")
def sql_delete():
    concept_name = "SQL Delete"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-delete.html", question=question, answers=answers, exercise=exercises)


# Joining Tables
@pages.route("/sql-aliases")
def sql_aliases():
    concept_name = "SQL Aliases"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-aliases.html", question=question, answers=answers, exercise=exercises)


@pages.route("/sql-joins")
def sql_joins():
    concept_name = "SQL Joins"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-joins.html", question=question, answers=answers, exercise=exercises)


@pages.route("/sql-inner-join")
def sql_inner_join():
    concept_name = "SQL Inner Join"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-inner-join.html", question=question, answers=answers, exercise=exercises)


@pages.route("/sql-left-join")
def sql_left_join():
    concept_name = "SQL Left Join"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-left-join.html", question=question, answers=answers, exercise=exercises)


@pages.route("/sql-right-join")
def sql_right_join():
    concept_name = "SQL Right Join"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-right-join.html", question=question, answers=answers, exercise=exercises)


@pages.route("/sql-full-join")
def sql_full_join():
    concept_name = "SQL Full Join"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-full-join.html", question=question, answers=answers, exercise=exercises)


@pages.route("/sql-union")
def sql_union():
    concept_name = "SQL Union"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-union.html", question=question, answers=answers, exercise=exercises)


# Table Management
@pages.route("/sql-constraints")
def sql_constraints():
    concept_name = "SQL Constraints"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-constraints.html", question=question, answers=answers, exercise=exercises)


@pages.route("/sql-create-table")
def sql_create_table():
    concept_name = "Create Tables"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-create-table.html", question=question, answers=answers, exercise=exercises)


@pages.route("/sql-alter-table")
def sql_alter_table():
    concept_name = "Alter Tables"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-alter-table.html", question=question, answers=answers, exercise=exercises)


@pages.route("/sql-drop-table")
def sql_drop_table():
    concept_name = "Drop Tables"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-drop-table.html", question=question, answers=answers, exercise=exercises)


@pages.route("/sql-truncate")
def sql_truncate():
    concept_name = "TRUNCATE Tables"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-truncate.html", question=question, answers=answers, exercise=exercises)


# Advanced SQL Techniques
@pages.route("/sql-subqueries")
def sql_subqueries():
    concept_name = "SQL Subqueries"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-subqueries.html", question=question, answers=answers, exercise=exercises)


@pages.route("/sql-window-functions")
def sql_window_functions():
    concept_name = "SQL Window Functions"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-window-functions.html", question=question, answers=answers, exercise=exercises)


@pages.route("/sql-case-statements")
def sql_case_statements():
    concept_name = "SQL CASE Statements"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-case-statements.html", question=question, answers=answers, exercise=exercises)


@pages.route("/sql-functions")
def sql_functions():
    concept_name = "SQL Functions"
    question, answers, exercises = get_concept_data(concept_name)
    return render_template("sql-functions.html", question=question, answers=answers, exercise=exercises)
