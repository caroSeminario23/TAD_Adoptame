package com.adoptame.albergue2.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;
import java.util.Optional;

import com.adoptame.albergue2.model.CaracteristicaComplementaria;
import com.adoptame.albergue2.repository.CarComplementariaRepository;

@Service
public class CarComplementariaService {
    @Autowired
    private CarComplementariaRepository carComplementariaRepository;

    public List<CaracteristicaComplementaria> obtenerTodasLasCaracteristicasComplementarias() {
        return carComplementariaRepository.findAll();
    }

    public Optional<CaracteristicaComplementaria> obtenerCaracteristicaComplementariaPorId(Integer id) {
        return carComplementariaRepository.findById(id);
    }
}
