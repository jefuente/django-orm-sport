from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),

		"ligas_baseball": League.objects.filter(sport__contains="baseball"),
		"ligas_mujeres": League.objects.filter(name__contains="Womens"),
		"ligas_hockey": League.objects.filter(sport__contains="hockey"),
		"ligas_no_football": League.objects.exclude(sport__contains="football"),
		"conferencias": League.objects.filter(name__contains="conference"),
		"atlantica": League.objects.filter(name__contains="Atlantic"),
		"teams_dallas": Team.objects.filter(location__contains="Dallas"),
		"teams_raptors": Team.objects.filter(team_name__contains="Raptors"),
		"teams_city": Team.objects.filter(location__contains="City"),
		"teams_t": Team.objects.filter(team_name__startswith='T'),
		"teams_ordenlocation": Team.objects.order_by("location"),
		"teams_ordeninverso": Team.objects.order_by("team_name").reverse(),
		"players_cooper": Player.objects.filter(last_name__contains="Cooper"),
		"players_joshua": Player.objects.filter(first_name__contains="Joshua"),
		"players_cooper_excepto_joshua": Player.objects.filter(last_name__contains="Cooper").exclude(first_name__icontains="Joshua"),
		"players_Alexander_or_Wyatt": Player.objects.filter(first_name__contains="Alexander")|Player.objects.filter(first_name__contains="Wyatt"),

		"teams_atlantic": Team.objects.filter(league=League.objects.get(name="Atlantic Soccer Conference")),
		"players_bostons": Player.objects.filter(curr_team=Team.objects.get(location="Boston", team_name= "Penguins")),
		"players_international": Player.objects.filter(curr_team__in=Team.objects.filter(league__in=(League.objects.filter(name="International Collegiate Baseball Conference")))),
		"players_conferencia_lopez": Player.objects.filter(curr_team__in=Team.objects.filter(league__in=(League.objects.filter(name="American Conference of Amateur Football")))),
		"players_futbol": Player.objects.filter(all_teams__in=Team.objects.filter(league__in=(League.objects.filter(name__contains="Football")))),
		"teams_sophia": Team.objects.filter(team_name__in=Player.objects.filter(first_name__contains="Sophia")),
		"leagues_sophia": League.objects.filter(name__in=Player.objects.filter(first_name__contains="Sophia")),
		#"players_flores_no": Player.objects.filter(last_name__contains="Flores").exclude(Team.objects.filter(team_name__contains= "Washington Roughriders")),
		#"teams_samuel"
		#"players_gatos"
		#"players_wichita_old"
		#"team_gray"
		#"players_joshua_no"
		#"teams_12"
		


	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")