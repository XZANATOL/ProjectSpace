package dev.xzanatol.miniBnB.Repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import dev.xzanatol.miniBnB.Model.RolesModel;

@Repository
public interface RolesRepo extends JpaRepository<RolesModel, Long> {
    // spring provides all the basic crud operations. No Coding!
}