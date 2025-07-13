package com.adoptame.albergue2.model;

import java.io.Serializable;
import java.util.Objects;
import jakarta.persistence.*;

@Embeddable
public class CaracteristicaMascotaId implements Serializable {

    @Column(name = "id_mascota")
    private Integer idMascota;

    @Column(name = "id_caracteristica")
    private Integer idCaracteristica;

    public CaracteristicaMascotaId() {}

    public CaracteristicaMascotaId(Integer idMascota, Integer idCaracteristica) {
        this.idMascota = idMascota;
        this.idCaracteristica = idCaracteristica;
    }

    // hashCode y equals obligatorios para claves compuestas
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof CaracteristicaMascotaId)) return false;
        CaracteristicaMascotaId that = (CaracteristicaMascotaId) o;
        return Objects.equals(idMascota, that.idMascota) &&
               Objects.equals(idCaracteristica, that.idCaracteristica);
    }

    @Override
    public int hashCode() {
        return Objects.hash(idMascota, idCaracteristica);
    }

    // Getters y setters si los necesitas
}
