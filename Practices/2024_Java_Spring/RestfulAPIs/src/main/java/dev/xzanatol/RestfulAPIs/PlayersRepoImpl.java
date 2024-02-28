package dev.xzanatol.RestfulAPIs;

import jakarta.persistence.EntityManager;
import jakarta.persistence.PersistenceContext;
import jakarta.transaction.Transactional;

import org.springframework.stereotype.Component;
import org.springframework.stereotype.Repository;

@Repository
@Component
public class PlayersRepoImpl implements PlayersRepo {

	@PersistenceContext
	private EntityManager entityManager;

	@Transactional
	public void customInsertPlayer(String name, int attack, int defense) {
        PlayersModel newPlayer = new PlayersModel(name, attack, defense);
        this.entityManager.persist(newPlayer);
    }

    public PlayersModel findPlayerByID(int id) {
	    return entityManager.find(PlayersModel.class, id);
	}

	@Transactional
	public void updatePlayerName(int id, String newName) {
		PlayersModel player = this.entityManager.find(PlayersModel.class, id);
		if(player != null){
			player.setName(newName);
			this.entityManager.merge(player);
		}
	}

	@Transactional
	public void deletePlayer(int id){
		PlayersModel player = this.entityManager.find(PlayersModel.class, id);
		if(player != null){
			this.entityManager.remove(player);
		}
	}


}