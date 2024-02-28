package dev.xzanatol.RestfulAPIs;

import org.springframework.stereotype.Repository;

@Repository
public interface PlayersRepo {
	
	void customInsertPlayer(String name, int attack, int defense);
	PlayersModel findPlayerByID(int id);
	void updatePlayerName(int id, String name);
	void deletePlayer(int id);

}