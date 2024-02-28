package dev.xzanatol.miniBnB.Controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import dev.xzanatol.miniBnB.Model.UserModel;
import dev.xzanatol.miniBnB.Model.RolesModel;
import dev.xzanatol.miniBnB.Service.AuthService;

import java.util.List;
import java.util.Optional;

@RestController
public class AuthController {
	private AuthService authService;

	@Autowired
	public void AuthController(AuthService authService){
		this.authService = authService;
	}

	@PostMapping("addUser")
	public ResponseEntity<UserModel> createUser(@RequestBody UserModel userModel){
		UserModel savedModel = authService.saveUser(userModel);
		return new ResponseEntity<>(savedModel, HttpStatus.CREATED);
	}
}