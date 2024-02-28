package dev.xzanatol.miniBnB.Controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import dev.xzanatol.miniBnB.Model.PropertyModel;
import dev.xzanatol.miniBnB.Service.PropertyService;
import dev.xzanatol.miniBnB.Exception.BookNotFoundException;

import java.util.List;
import java.util.Optional;

@RestController
public class Routes {

    private PropertyService propertyService;

    @Autowired
    public void PropertyController(PropertyService propertyService) {
        this.propertyService = propertyService;
    }

    @PostMapping("properties")
    public ResponseEntity<PropertyModel> createProperty(@RequestBody PropertyModel propertyModel) {
        PropertyModel savedProperty = propertyService.saveProperty(propertyModel);
        return new ResponseEntity<>(savedProperty, HttpStatus.CREATED);
    }

    @GetMapping("/properties")
    public ResponseEntity<List<PropertyModel>> getAllProperties() {
        List<PropertyModel> properties = propertyService.getAllProperties();
        return new ResponseEntity<>(properties, HttpStatus.OK);
    }

    @GetMapping("/properties/{id}")
    public ResponseEntity<PropertyModel> getPropertyById(@PathVariable Long id) {
        if(id < 0){
            throw new BookNotFoundException("BnB Not Found", "BnB with ID " + id + " not found");
        }else{
            return propertyService.getPropertyById(id)
                    .map(property -> new ResponseEntity<>(property, HttpStatus.OK))
                    .orElseGet(() -> new ResponseEntity<>(HttpStatus.NOT_FOUND));
        }
    }

    @DeleteMapping("properties/{id}")
    public ResponseEntity<Void> deleteProperty(@PathVariable Long id) {
        propertyService.deleteProperty(id);
        return new ResponseEntity<>(HttpStatus.NO_CONTENT);
    }

    @PutMapping("/updateName")
    public ResponseEntity<PropertyModel> updatePropertyName(
            @RequestParam(name = "id") Long id,
            @RequestParam(name = "name") String name) {

        // Retrieve the existing property
        Optional<PropertyModel> optionalProperty = propertyService.getPropertyById(id);
        if (optionalProperty.isPresent()) {
            PropertyModel existingProperty = optionalProperty.get();

            // Update the name of the property
            existingProperty.setName(name);

            // Save the updated property
            PropertyModel updatedProperty = propertyService.saveProperty(existingProperty);
            return new ResponseEntity<>(updatedProperty, HttpStatus.OK);
        } else {
            // PropertyModel not found
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }
}