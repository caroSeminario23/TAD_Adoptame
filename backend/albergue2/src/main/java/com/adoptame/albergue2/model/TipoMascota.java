package com.adoptame.albergue2.model;

import jakarta.persistence.*;

@Entity
@Table(name = "tipo_mascota", schema = "SYSTEM")
public class TipoMascota {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id_tipo_mascota", nullable = false)
    private Integer idTipoMascota;

    @Column(name = "nombre", nullable = false, unique = true, length = 20)
    private String nombre;

    // Constructor vacío (necesario para JPA)
    public TipoMascota() {
    }

    // Constructor con parámetros
    public TipoMascota(String nombre) {
        this.nombre = nombre;
    }

    // Getters y setters
    public Integer getIdTipoMascota() {
        return idTipoMascota;
    }

    public void setIdTipoMascota(Integer idTipoMascota) {
        this.idTipoMascota = idTipoMascota;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
}
