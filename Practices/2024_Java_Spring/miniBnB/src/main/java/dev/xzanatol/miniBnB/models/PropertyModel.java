package dev.xzanatol.miniBnB.Model;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Entity
@Table(name = "properties")
@Getter
@Setter
public class PropertyModel {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "name")
    private String name;

    @Column(name = "description")
    private String description;

    @Column(name = "price")
    private double price;

    // Other fields such as location, amenities, etc.

    // Constructors, getters, and setters
    PropertyModel(){}

    PropertyModel(String name, String description, double price){
        this.name = name;
        this.description = description;
        this.price = price;
    }
}