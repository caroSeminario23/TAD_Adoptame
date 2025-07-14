package com.adoptame.albergue2.dto;

public class CarateristicaComplementariaDTO {
    private Integer idCaracteristica;
    private String nombre;
    private String unidadMedida;

    public CarateristicaComplementariaDTO() {}

    public CarateristicaComplementariaDTO(Integer idCaracteristica, 
                                        String nombre, 
                                        String unidadMedida) {
        this.idCaracteristica = idCaracteristica;
        this.nombre = nombre;
        this.unidadMedida = unidadMedida;
    }

    // Getters y setters
    public Integer getIdCaracteristica() {
        return idCaracteristica;
    }
    public void setIdCaracteristica(Integer idCaracteristica) {
        this.idCaracteristica = idCaracteristica;
    }
    public String getNombre() {
        return nombre;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getUnidadMedida() {
        return unidadMedida;
    }
    public void setUnidadMedida(String unidadMedida) {
        this.unidadMedida = unidadMedida;
    }
}
