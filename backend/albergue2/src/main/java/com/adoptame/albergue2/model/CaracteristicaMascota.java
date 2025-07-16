package com.adoptame.albergue2.model;

import jakarta.persistence.*;

@Entity
@Table(name = "CARACTERISTICA_MASCOTA")
public class CaracteristicaMascota {
    @EmbeddedId
    private CaracteristicaMascotaId id;

    @ManyToOne
    @MapsId("idMascota")
    @JoinColumn(name = "ID_MASCOTA", nullable = false)
    private Mascota mascota;

    @ManyToOne
    @MapsId("idCaracteristica")
    @JoinColumn(name = "ID_CARACTERISTICA", nullable = false)
    private CaracteristicaComplementaria caracteristica;

    @Column(name = "VALOR", nullable = false, length = 25)
    private String valor;

    // Constructor vacío (necesario para JPA)
    public CaracteristicaMascota() {
    }

    // Constructor con parámetros
    public CaracteristicaMascota(Mascota mascota,
                                CaracteristicaComplementaria caracteristica, 
                                String valor) {
        this.id = new CaracteristicaMascotaId(mascota.getIdMascota(), caracteristica.getIdCaracteristica());
        this.mascota = mascota;
        this.caracteristica = caracteristica;
        this.valor = valor;
    }

    // Getters y setters
    public CaracteristicaMascotaId getId() {
        return id;
    }

    public void setId(CaracteristicaMascotaId id) {
        this.id = id;
    }

    public Mascota getMascota() {
        return mascota;
    }

    public void setMascota(Mascota mascota) {
        this.mascota = mascota;
        this.id.setIdMascota(mascota.getIdMascota());
    }

    public CaracteristicaComplementaria getCaracteristica() {
        return caracteristica;
    }

    public void setCaracteristica(CaracteristicaComplementaria caracteristica) {
        this.caracteristica = caracteristica;
        this.id.setIdCaracteristica(caracteristica.getIdCaracteristica());
    }

    public String getValor() {
        return valor;
    }

    public void setValor(String valor) {
        this.valor = valor;
    }
}
