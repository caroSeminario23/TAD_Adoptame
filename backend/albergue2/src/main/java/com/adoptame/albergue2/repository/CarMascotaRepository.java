package com.adoptame.albergue2.repository;

import com.adoptame.albergue2.model.CaracteristicaMascota;
import com.adoptame.albergue2.model.CaracteristicaMascotaId;
import org.springframework.stereotype.Repository;
import org.springframework.data.jpa.repository.JpaRepository;

@Repository
public interface CarMascotaRepository extends JpaRepository<CaracteristicaMascota, CaracteristicaMascotaId> {

}
