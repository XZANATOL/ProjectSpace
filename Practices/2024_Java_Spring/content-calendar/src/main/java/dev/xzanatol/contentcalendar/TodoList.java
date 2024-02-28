package dev.xzanatol.contentcalendar;

import java.util.ArrayList;

import org.springframework.stereotype.Component;
import org.springframework.context.annotation.Lazy;

/*
import org.springframework.beans.factory.config.ConfigurableBeanFactory;
import org.springframework.context.annotation.Scope;
*/

@Component
@Lazy
//@Scope(ConfigurableBeanFactory.SCOPE_PROTOTYPE) <= if you want seperate instances
public class TodoList implements ListInterface {
	private ArrayList<String> tasks = new ArrayList<>();

	TodoList() {
		this.tasks.add("Learn Java");
		this.tasks.add("Learn Odoo");
	}

	public ArrayList<String> getTasks() {
		return this.tasks;
	}

}