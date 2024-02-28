package dev.xzanatol.contentcalendar;

import java.util.ArrayList;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.beans.factory.annotation.Autowired;

@RestController
public class RouteController {
	private ListInterface tasks;
	private ThirdParty thirdParty;

	@Autowired
	RouteController(@Qualifier("todoList") ListInterface listInterface, ThirdParty TH){
		this.tasks = listInterface;
		this.thirdParty = TH;
	}

	@RequestMapping("/")
	public String home() { return "XZANATOL"; }

	@RequestMapping("/tasks")
	public ArrayList<String> getAllTasks() {
		this.thirdParty.performAction();
		return this.tasks.getTasks();
	}
}