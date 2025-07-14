package com.adoptame.albergue2.dto;

public class CaracteristicaMascotaDTO {
    private Integer idMascota;
    private Integer idCaracteristica;
    private String valor;

    public CaracteristicaMascotaDTO() {}

    public CaracteristicaMascotaDTO(Integer idMascota, 
                                    Integer idCaracteristica, 
                                    String valor) {
        this.idMascota = idMascota;
        this.idCaracteristica = idCaracteristica;
        this.valor = valor;
    }

    // Getters y setters
    public Integer getIdMascota() { 
        return idMascota; 
    }
    public void setIdMascota(Integer idMascota) { 
        this.idMascota = idMascota; 
    }
    public Integer getIdCaracteristica() { 
        return idCaracteristica; 
    }
    public void setIdCaracteristica(Integer idCaracteristica) { 
        this.idCaracteristica = idCaracteristica; 
    }
    public String getValor() { 
        return valor; 
    }
    public void setValor(String valor) { 
        this.valor = valor; 
    }
}
