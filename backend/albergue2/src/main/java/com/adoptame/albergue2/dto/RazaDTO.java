package com.adoptame.albergue2.dto;

public class RazaDTO {
    private Integer idRaza;
    private String nombre;

    public RazaDTO() {}

    public RazaDTO(Integer idRaza, String nombre) {
        this.idRaza = idRaza;
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
