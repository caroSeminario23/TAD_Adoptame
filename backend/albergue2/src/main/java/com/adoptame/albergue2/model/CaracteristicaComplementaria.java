package com.adoptame.albergue2.model;

import jakarta.persistence.*;

@Entity
@Table(name = "caracteristica_complementaria")
public class CaracteristicaComplementaria {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id_caracteristica", nullable = false)
    private Integer idCaracteristica;

    @Column(name = "nombre", nullable = false, unique = true, length = 15)
    private String nombre;

    @Column(name = "unidad_medida", nullable = false, length = 7)
    private String unidadMedida;

    // Constructor vacío (necesario para JPA)
    public CaracteristicaComplementaria() {
    }

    // Constructor con parámetros
    public CaracteristicaComplementaria(String nombre, 
                                        String unidadMedida) {
        this.nombre = nombre;
        this.unidadMedida = unidadMedida;
    }
}
