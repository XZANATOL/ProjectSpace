package dev.xzanatol.miniBnB.Service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import dev.xzanatol.miniBnB.Model.UserModel;
import dev.xzanatol.miniBnB.Model.RolesModel;
import dev.xzanatol.miniBnB.Repository.UserRepo;
import dev.xzanatol.miniBnB.Repository.RolesRepo;

import java.util.List;
import java.util.Optional;

@Service
public class AuthService {
	private final UserRepo userRepo;
	private final RolesRepo rolesRepo;

	@Autowired
	public AuthService(UserRepo userRepo, RolesRepo rolesRepo){
		this.userRepo = userRepo;
		this.rolesRepo = rolesRepo;
	}

	public UserModel saveUser(UserModel user){
		user.encryptPass();
		UserModel savedUser = userRepo.save(user);
		RolesModel rolesModel = new RolesModel(savedUser.getId(), "USER"); 
		rolesRepo.save(rolesModel);
		return savedUser;
	}
}