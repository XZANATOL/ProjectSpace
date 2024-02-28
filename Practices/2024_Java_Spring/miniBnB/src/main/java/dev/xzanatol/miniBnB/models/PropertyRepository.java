package dev.xzanatol.miniBnB.Repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import dev.xzanatol.miniBnB.Model.PropertyModel;

@Repository
public interface PropertyRepository extends JpaRepository<PropertyModel, Long> {
    // spring provides all the basic crud operations. No Coding!
}