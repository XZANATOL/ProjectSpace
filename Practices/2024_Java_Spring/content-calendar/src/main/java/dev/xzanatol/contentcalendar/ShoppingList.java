package dev.xzanatol.contentcalendar;

import java.util.ArrayList;

import org.springframework.stereotype.Component;
import org.springframework.context.annotation.Lazy;

@Component
@Lazy
public class ShoppingList implements ListInterface {
	private ArrayList<String> tasks = new ArrayList<>();

	ShoppingList() {
		this.tasks.add("Bug Oracle");
		this.tasks.add("Kill MT");
	}

	public ArrayList<String> getTasks() {
		return this.tasks;
	}
}