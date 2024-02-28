package dev.xzanatol.miniBnB.Service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import dev.xzanatol.miniBnB.Model.PropertyModel;
import dev.xzanatol.miniBnB.Repository.PropertyRepository;

import java.util.List;
import java.util.Optional;

@Service
public class PropertyService {

    private final PropertyRepository propertyRepository;

    @Autowired
    public PropertyService(PropertyRepository propertyRepository) {
        this.propertyRepository = propertyRepository;
    }

    public List<PropertyModel> getAllProperties() {
        return propertyRepository.findAll();
    }

    public Optional<PropertyModel> getPropertyById(Long id) {
        return propertyRepository.findById(id);
    }

    public PropertyModel saveProperty(PropertyModel property) {
        return propertyRepository.save(property);
    }

    public void deleteProperty(Long id) {
        propertyRepository.deleteById(id);
    }

    // You can add more methods based on your business logic and requirements
}