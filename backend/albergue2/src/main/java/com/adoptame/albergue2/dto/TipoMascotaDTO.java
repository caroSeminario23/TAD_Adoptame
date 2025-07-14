package com.adoptame.albergue2.dto;

public class TipoMascotaDTO {
    private Integer idTipoMascota;
    private String nombre;

    public TipoMascotaDTO() {}

    public TipoMascotaDTO(Integer idTipoMascota, String nombre) {
        this.idTipoMascota = idTipoMascota;
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
