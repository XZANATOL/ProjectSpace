package dev.xzanatol.RestfulAPIs;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class PlayersController {
	
	private PlayersRepo playersRepo;

	@Autowired
	public void PlayerController(PlayersRepo playersRepo){
		this.playersRepo = playersRepo;
	}

	@GetMapping("/newplayer")
	public String newPlayer(@RequestParam String name, @RequestParam int attack, @RequestParam int defense){
		this.playersRepo.customInsertPlayer(name, attack, defense);
		return "New player added!";
	}

	@GetMapping("/getplayer")
	public String getPlayer(@RequestParam int id) {
	    PlayersModel player = this.playersRepo.findPlayerByID(id);
	    return player.getName();
	}

	@GetMapping("/updateplayer")
	public String updateName(@RequestParam int id, @RequestParam String name){
		this.playersRepo.updatePlayerName(id, name);
		return "Player name updated!";
	}

	@GetMapping("/deleteplayer")
	public String deletePlayer(@RequestParam int id){
		this.playersRepo.deletePlayer(id);
		return "Player deleted!";
	}

}