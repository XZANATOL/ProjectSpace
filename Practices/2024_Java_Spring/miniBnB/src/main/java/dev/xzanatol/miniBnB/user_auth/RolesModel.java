package dev.xzanatol.miniBnB.Model;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Entity
@Table(name = "roles")
@Getter
@Setter
public class RolesModel {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "username_id")
    private long username_id;

    @Column(name = "role")
    private String role;

    RolesModel(){}

    public RolesModel(long username_id, String role){
        this.username_id = username_id;
        this.role = role;
    }

    public void setRoleUSER(long id){
        this.role = "ROLE_USER";
        this.username_id = id;
    }
}