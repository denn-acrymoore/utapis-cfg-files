import unittest
from cfg_initialization import cfg_true_or_false


class TestKonjAtr(unittest.TestCase):
    def test_kj_atr_1_kata_01(self):
        """
        -> Konjungsi Antar Kalimat 1 Kata - 01
        (Kemudian, kj_atr_pertama), (,, td_koma),
        (masukkan, verba), (telur, nomina),
        (ke, preposisi), (dalam, nomina),
        (adonan, nomina), (., td_akhir_kal)
        """
        kal = [
            "<kj_atr_pertama>",
            "<td_koma>",
            "<verba>",
            "<nomina>",
            "<preposisi>",
            "<nomina>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_kj_atr_1_kata_02(self):
        """
        -> Konjungsi Antar Kalimat 1 Kata - 02
        (Sebenarnya, kj_atr_pertama), (,, td_koma),
        (kasus, nomina), (yang, kj_sub_yang), (serupa, nomina),
        (sudah, adverbia), (pernah, adverbia), (terjadi, verba),
        (sebelumnya, nomina), (., td_akhir_kal)
        """
        kal = [
            "<kj_atr_pertama>",
            "<td_koma>",
            "<nomina>",
            "<kj_sub_yang>",
            "<nomina>",
            "<adverbia>",
            "<adverbia>",
            "<verba>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_kj_atr_2_kata_01(self):
        """
        -> Konjungsi Antar Kalimat 2 Kata - 01
        (Biarpun, kj_atr_pertama), (demikian, kj_atr_kedua),
        (,, td_koma), (artis, nomina), (tersebut, verba),
        (tetap, adverbia), (menjalani, verba), (operasi, nomina),
        (tersebut, verba), (., td_akhir_kal)
        """
        kal = [
            "<kj_atr_pertama>",
            "<kj_atr_kedua>",
            "<td_koma>",
            "<nomina>",
            "<verba>",
            "<adverbia>",
            "<verba>",
            "<nomina>",
            "<verba>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_kj_atr_2_kata_02(self):
        """
        -> Konjungsi Antar Kalimat 2 Kata - 02
        (Bagaimanapun, kj_atr_pertama), (juga, kj_atr_kedua),
        (,, td_koma), (perlombaan, nomina), (ASEAN, nomina),
        (2023, numeralia), (akan, adverbia), (dihentikan, verba),
        (sementara, nomina), (., td_akhir_kal)
        """
        kal = [
            "<kj_atr_pertama>",
            "<kj_atr_kedua>",
            "<td_koma>",
            "<nomina>",
            "<nomina>",
            "<numeralia>",
            "<adverbia>",
            "<verba>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_kj_atr_3_kata_01(self):
        """
        -> Konjungsi Antar Kalimat 3 Kata - 01
        (Tak, kj_atr_pertama), (hanya, kj_atr_kedua),
        (itu, kj_atr_ketiga), (,, td_koma), (paman, nomina),
        (juga, adverbia), (mengalami, verba), (sakit, adjektiva),
        (diare, nomina), (., td_akhir_kal)
        """
        kal = [
            "<kj_atr_pertama>",
            "<kj_atr_kedua>",
            "<kj_atr_ketiga>",
            "<td_koma>",
            "<nomina>",
            "<adverbia>",
            "<verba>",
            "<adjektiva>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_kj_atr_3_kata_02(self):
        """
        -> Konjungsi Antar Kalimat 3 Kata - 02
        (Terkait, kj_atr_pertama), (hal, kj_atr_kedua), (ini, kj_atr_ketiga),
        (,, td_koma), (dia, nomina), (sudah, adverbia), (mendapatkan, verba),
        (dukungan, nomina), (dari, preposisi), (rakyat, nomina), (., td_akhir_kal)
        """
        kal = [
            "<kj_atr_pertama>",
            "<kj_atr_kedua>",
            "<kj_atr_ketiga>",
            "<td_koma>",
            "<nomina>",
            "<adverbia>",
            "<verba>",
            "<nomina>",
            "<preposisi>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_kj_atr_adapun_01(self):
        """
        -> Konjungsi Antar Kalimat "Adapun" - 01
        (Adapun, kj_atr_adapun), (saya, nomina), (ini, nomina),
        (disuruh, verba), (juga, adverbia), (olehnya, nomina),
        (meminta, verba), (bantuan, nomina), (., td_akhir_kal)
        """
        kal = [
            "<kj_atr_adapun>",
            "<nomina>",
            "<nomina>",
            "<verba>",
            "<adverbia>",
            "<nomina>",
            "<verba>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_kj_atr_adapun_02(self):
        """
        -> Konjungsi Antar Kalimat "Adapun" - 02
        (Adapun, kj_atr_adapun), (tugas, nomina), (ini, nomina),
        (harus, adverbia), (diselesaikan, verba), (besok, nomina),
        (., td_akhir_kal)
        """
        kal = [
            "<kj_atr_adapun>",
            "<nomina>",
            "<nomina>",
            "<adverbia>",
            "<verba>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_kj_atr_adapun_03(self):
        """
        -> Konjungsi Antar Kalimat "Adapun" - 03
        (Adapun, kj_atr_adapun), (,, td_koma), (sesuai, adjektiva), (perintah, nomina),
        (atasan, nomina), (,, td_koma), (tugas, nomina), (ini, nomina),
        (harus, adverbia), (diselesaikan, verba), (besok, nomina),
        (., td_akhir_kal)
        """
        kal = [
            "<kj_atr_adapun>",
            "<td_koma>",
            "<adjektiva>",
            "<nomina>",
            "<nomina>",
            "<td_koma>",
            "<nomina>",
            "<nomina>",
            "<adverbia>",
            "<verba>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))
