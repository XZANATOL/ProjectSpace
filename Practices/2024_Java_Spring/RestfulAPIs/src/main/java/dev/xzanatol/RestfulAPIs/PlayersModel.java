package dev.xzanatol.RestfulAPIs;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@Entity
public class PlayersModel {

	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	private long id;
	private String name;
	private int attack;
	private int defense;

	PlayersModel(){}

	PlayersModel(String name, int attack, int defense){
		this.name = name;
		this.attack = attack;
		this.defense = defense;
	}

	String getName(){
		return this.name;
	}

	void setName(String name){
		this.name = name;
	}


}