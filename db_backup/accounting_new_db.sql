-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : lun. 11 nov. 2024 à 08:15
-- Version du serveur : 10.4.28-MariaDB
-- Version de PHP : 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `accounting_new_db`
--

-- --------------------------------------------------------

--
-- Structure de la table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('52d29383c568');

-- --------------------------------------------------------

--
-- Structure de la table `blacklisted_tokens`
--

CREATE TABLE `blacklisted_tokens` (
  `id` int(11) NOT NULL,
  `jti` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `code_debit`
--

CREATE TABLE `code_debit` (
  `code_debit` varchar(11) NOT NULL,
  `budget` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `firstname` varchar(50) NOT NULL,
  `lastname` varchar(50) NOT NULL,
  `role` varchar(50) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`id`, `firstname`, `lastname`, `role`, `email`, `password`) VALUES
(1, 'John', 'Doe', 'user', 'john.doe@example.com', ''),
(3, 'admin', 'Doe', 'user', 'admin.doe@example.com', 'scrypt:32768:8:1$Qhcnlm5Ei6eLeN6h$360850c7c5716de5cc5b960c2f5c08'),
(4, 'test', 'test', 'user', 'test.doe@example.com', 'scrypt:32768:8:1$4AjDJ1qZmoEreVYW$314e3c0b732953af71a770d7d076582a925385331e813faa58163e5040270aed96033761005fc5f4fdeb9e31ef57c8d7beefd6f1cda59aa4a45973b3cd34670a'),
(5, 'derick', 'test', 'user', 'derick.doe@example.com', 'scrypt:32768:8:1$KlANDjJ0ARHJnH2r$fa23e2639da07d34a470aafbdbb674715561bfc2b0245d636301205f9bcf2170bad904b5a88369d2f7c0ac6190e383ece91f145ae0966da15d2639eeb5b34f9f'),
(6, 'figo', 'figo', 'user', 'figo.doe@example.com', 'scrypt:32768:8:1$1J7a5Jk6o6n4k02f$0b362c1bb94537e03029372504b396d70809a0e0345df6ee4c59e2c58def4b60d147f8a26971b913b65f6a4dd3b1a82f2df3fd2ff90e16841069d629d756d2c4');

-- --------------------------------------------------------

--
-- Structure de la table `vouchers`
--

CREATE TABLE `vouchers` (
  `id` int(11) NOT NULL,
  `debit_amount` float NOT NULL,
  `credit_amount` float NOT NULL,
  `debit_code` varchar(11) NOT NULL,
  `credit_code` varchar(11) NOT NULL,
  `label` text NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `vouchers`
--

INSERT INTO `vouchers` (`id`, `debit_amount`, `credit_amount`, `debit_code`, `credit_code`, `label`, `user_id`, `created_at`) VALUES
(2, 1, 1, '01', '01', 'test', 6, '2024-10-26 10:06:27'),
(3, 100, 100, 'D001', 'C001', 'Test Voucher', 6, '2024-10-26 10:06:27'),
(4, 100, 100, 'D001', 'C001', 'Test Voucher', 6, '2024-10-26 10:06:27'),
(5, 100, 100, 'D001', 'C001', 'Test Voucher', 6, '2024-10-26 07:07:01'),
(6, 100, 100, 'D001', 'C001', 'Test Voucher', 6, '2024-10-26 07:10:32');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Index pour la table `blacklisted_tokens`
--
ALTER TABLE `blacklisted_tokens`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `jti` (`jti`);

--
-- Index pour la table `code_debit`
--
ALTER TABLE `code_debit`
  ADD PRIMARY KEY (`code_debit`);

--
-- Index pour la table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Index pour la table `vouchers`
--
ALTER TABLE `vouchers`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `debit_code` (`debit_code`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `blacklisted_tokens`
--
ALTER TABLE `blacklisted_tokens`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT pour la table `vouchers`
--
ALTER TABLE `vouchers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `vouchers`
--
ALTER TABLE `vouchers`
  ADD CONSTRAINT `vouchers_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
