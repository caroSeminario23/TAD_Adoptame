package com.adoptame.albergue2.model;

import jakarta.persistence.*;

@Entity
@Table(name = "caracteristica_mascota")
public class CaracteristicaMascota {
    @Id
    @ManyToOne
    @JoinColumn(name = "id_mascota", nullable = false)
    private Mascota mascota;

    @Id
    @ManyToOne
    @JoinColumn(name = "id_caracteristica", nullable = false)
    private CaracteristicaComplementaria caracteristica;

    @Column(name = "valor", nullable = false, length = 25)
    private String valor;

    // Constructor vacío (necesario para JPA)
    public CaracteristicaMascota() {
    }

    // Constructor con parámetros
    public CaracteristicaMascota(Mascota mascota,
                                CaracteristicaComplementaria caracteristica, 
                                String valor) {
        this.mascota = mascota;
        this.caracteristica = caracteristica;
        this.valor = valor;
    }
}
