package com.adoptame.albergue2.model;

import jakarta.persistence.*;

@Entity
@Table(name = "RAZA")
public class Raza {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "ID_RAZA", nullable = false)
    private Integer idRaza;

    @Column(name = "NOMBRE", nullable = false, unique = true, length = 20)
    private String nombre;

    // Constructor vacío (necesario para JPA)
    public Raza() {
    }

    // Constructor con parámetros
    public Raza(String nombre) {
        this.nombre = nombre;
    }

    // Getters y setters
    public Integer getIdRaza() {
        return idRaza;
    }

    public void setIdRaza(Integer idRaza) {
        this.idRaza = idRaza;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
}
