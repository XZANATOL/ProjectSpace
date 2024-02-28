package dev.xzanatol.miniBnB.Model;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Entity
@Table(name = "user")
@Getter
@Setter
public class UserModel {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "username")
    private String username;

    @Column(name = "password")
    private String password;

    @Column(name = "is_active")
    private boolean is_active;

    UserModel(){}

    UserModel(String username, String password, boolean is_active){
        this.username = username;
        this.password = password;
        this.is_active = is_active;
    }

    public void encryptPass(){
        this.password = "[noop]" + this.password;
    }

    public long getId(){
        return this.id;
    }
}