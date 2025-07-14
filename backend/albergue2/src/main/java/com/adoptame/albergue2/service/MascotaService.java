package com.adoptame.albergue2.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

import com.adoptame.albergue2.dto.MascotaDTO;
import com.adoptame.albergue2.dto.RazaDTO;
import com.adoptame.albergue2.dto.TipoMascotaDTO;
import com.adoptame.albergue2.model.Mascota;
import com.adoptame.albergue2.model.Raza;
import com.adoptame.albergue2.model.TipoMascota;
import com.adoptame.albergue2.repository.MascotaRepository;

@Service
public class MascotaService {
    @Autowired
    private MascotaRepository mascotaRepository;

    // Método para convertir una entidad a DTO
    private MascotaDTO convertirADTO(Mascota entidad) {
        return new MascotaDTO(
            entidad.getIdMascota(),
            entidad.getNombre(),
            entidad.getFoto(),
            entidad.getFecNacimiento(),
            entidad.getSexo(),
            entidad.getEstatura(),
            entidad.getPeso(),
            convertirTipoMascotaADTO(entidad.getTipoMascota()),
            convertirRazaADTO(entidad.getRaza()),
            entidad.getFecIngreso(),
            entidad.getAdoptado(),
            entidad.getDiscapacidad()
        );
    }

    private TipoMascotaDTO convertirTipoMascotaADTO(TipoMascota tipo) {
        return new TipoMascotaDTO(tipo.getIdTipoMascota(), tipo.getNombre());
    }

    private RazaDTO convertirRazaADTO(Raza raza) {
        return new RazaDTO(raza.getIdRaza(), raza.getNombre());
    }

    // Devolver todas las mascotas como DTO
    public List<MascotaDTO> obtenerTodasLasMascotas() {
        return mascotaRepository.findAll()
                .stream()
                .map(this::convertirADTO)
                .collect(Collectors.toList());
    }

    // Devolver todas las características de mascotas
    public Optional<MascotaDTO> obtenerMascotaPorId(Integer id) {
        return mascotaRepository.findById(id).map(this::convertirADTO);
    }
}
