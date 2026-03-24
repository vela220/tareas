-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.32-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.16.0.7229
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Volcando datos para la tabla tareas.tarea: ~0 rows (aproximadamente)
INSERT INTO `tarea` (`id_tarea`, `id_usuario`, `Titulo`, `Descripcion`, `Fecha_creacion`, `Fecha_limite`, `Hora_limite`) VALUES
	(1, 1, 'Español', 'oraciones', '2026-03-20 02:07:17', '2026-03-19', '20:07:21');

-- Volcando datos para la tabla tareas.usuario: ~1 rows (aproximadamente)
INSERT INTO `usuario` (`id_usuario`, `Nombre`, `Apellido`, `Email`, `Password`, `Telefono`, `Fecha_registro`, `Ultimo_acceso`, `Activo`, `Foto_perfil`) VALUES
	(1, 'Esteban', 'Camacho', 'Camacho@gmail.com', '1234', '6568997489', '2023-03-20 01:54:40', '2026-03-20 01:55:00', 1, 'si');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
