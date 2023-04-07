from django.test import TestCase
from django.urls import reverse, resolve
from Benches.models import Benches, Audio
from Parks.models import Park


class TestModels(TestCase):
    
    # Set up a bench and park to test
    def setUp(self):
        self.bench1 = Benches.objects.create(
            bench_id = 1,
            bench_title = 'test bench',
            park_id = Park.objects.create(
                park_id = 1,
                name = 'test park',
                location = 'test location'
            )
        )
        self.audio1 = Audio.objects.create(
            audio_id = 1,
            bench_id = self.bench1,
            audio_binary = False,
            contributor = 'test contributor',
            length_category = "0-5",
            season_category = 'Spring'
        )
       
    # Testing the bench model
    def test_bench_model(self):
        self.assertEquals(self.bench1.bench_id, 1)
        self.assertEquals(self.bench1.bench_title, 'test bench')
        self.assertEquals(self.bench1.park_id.park_id, 1)
        self.assertEquals(self.bench1.park_id.name, 'test park')
        self.assertEquals(self.bench1.park_id.location, 'test location')
        
    # Testing the audio model
    def test_audio_model(self):
        self.assertEquals(self.audio1.audio_id, 1)
        self.assertEquals(self.audio1.bench_id.bench_id, 1)
        self.assertEquals(self.audio1.audio_binary, False)
        self.assertEquals(self.audio1.contributor, 'test contributor')
        self.assertEquals(self.audio1.length_category, "0-5"),
        self.assertEquals(self.audio1.season_category, 'Spring')
        
    # Testing the audio get_length_category function
    def test_get_length_category(self):
        self.assertEquals(self.audio1.get_length_category(), "0-5")
        
    # Testing the audio get_season_category function
    # def test_get_season_category(self):
    #     self.assertEquals(self.audio1.get_season_category(), Audio.Season_Category('Spring'))