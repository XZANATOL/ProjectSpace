package dev.xzanatol.miniBnB.Repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import dev.xzanatol.miniBnB.Model.UserModel;

@Repository
public interface UserRepo extends JpaRepository<UserModel, Long> {
    // spring provides all the basic crud operations. No Coding!
}