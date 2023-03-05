from pcconfig import config
import pynecone as pc

from . import models

vstack_css: dict = {
    "border_radius" : "md",
    "border": "1px solid black",
    "padding": "16px",
    "width": "100%"
}

class State(pc.State):
    """Manages behaviors of ToDo input fields"""
    text: str = ""
    todos: str = ""
    done: str = ""

    def set_record(self, text):
        self.text = text


    def add_record_todo(self):
        if self.text != "":
            with pc.session() as session:
                session.add(
                    models.ToDo(
                        title = self.text,
                        done = False
                    )
                )
                session.commit()
        return self.get_todo()


    def add_record_done(self):
        if self.text != "":
            with pc.session() as session:
                session.add(
                    models.ToDo(
                        title = self.text,
                        done = True
                    )
                )
                session.commit()
        return self.get_todo()


    def get_todo(self) -> None:
        todo_res: list
        done_res: list
        with pc.session() as session:
            todo_res = session.query(models.ToDo).filter(models.ToDo.done.contains(0)).all()
            done_res = session.query(models.ToDo).filter(models.ToDo.done.contains(1)).all()
        
        self.todos, self.done = ["", ""] 
        for query in todo_res:
            self.todos += f"* {query.title}\n"
        for query in done_res:
            self.done += f"* {query.title}\n"


@pc.route(route="/", title="PyneCone_Explore", on_load=State.get_todo)
def index() -> pc.Component:
    return pc.flex(
        pc.vstack(
            pc.heading("To-Do", size="lg"),
            pc.markdown(State.todos),
            pc.center(
                pc.input(
                    placeholder = "New record...",
                    on_change = State.set_record,
                    width = "50%"
                ),
                pc.button_group(
                    pc.button(
                        "Add",
                        border_radius="1em",
                        on_click = State.add_record_todo
                    ),

                    margin_left = "8px"
                ),

                width = "100%"
            ),                

            margin_left = "2%",
            margin_right = "1%",
            **vstack_css
        ),
        
        pc.vstack(
            pc.heading("Done", size="lg"),
            pc.markdown(State.done),
            pc.center(
                pc.input(
                    placeholder = "New record...",
                    on_change = State.set_record,
                    width = "50%"
                ),
                pc.button_group(
                    pc.button(
                        "Add",
                        border_radius="1em",
                        on_click = State.add_record_done
                    ),

                    margin_left = "8px"
                ),

                width = "100%"
            ),

            margin_left = "1%",
            margin_right = "2%",
            **vstack_css
        ),
        
        align = "center",
        justify = "space-around",
        padding_top="10%",
        )


# Note: using kebab-case is not supported,
# so check for errors on the console to fix them.
styles: dict = {
    pc.Heading: {
        "textDecoration": "underline"
    }
}

app = pc.App(state=State, style=styles)
app.compile()
