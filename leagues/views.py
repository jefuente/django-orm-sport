from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker
from django.db.models import Count

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
		"teams_ordeninverso": Team.objects.order_by("-team_name"),
		#"teams_ordeninverso": Team.objects.order_by("team_name").reverse(),
		"players_cooper": Player.objects.filter(last_name__contains="Cooper"),
		"players_joshua": Player.objects.filter(first_name__contains="Joshua"),
		"players_cooper_excepto_joshua": Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),
		"players_Alexander_or_Wyatt": Player.objects.filter(first_name__in=["Alexander", "Wyatt"]),
		#"players_Alexander_or_Wyatt": Player.objects.filter(first_name="Alexander")|Player.objects.filter(first_name="Wyatt"),
		#"players_Alexander_or_Wyatt": Player.objects.filter(Q(first_name="Alexander")|Q(first_name="Wyatt"),

		"teams_atlantic": Team.objects.filter(league=League.objects.get(name="Atlantic Soccer Conference")),
		"players_bostons": Player.objects.filter(curr_team=Team.objects.get(location="Boston", team_name= "Penguins")),
		"players_international": Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference"),
		#"players_international": Player.objects.filter(curr_team__in=Team.objects.filter(league__in=(League.objects.filter(name="International Collegiate Baseball Conference")))),
		"players_conferencia_lopez": Player.objects.filter(curr_team__league__name="American Conference of Amateur Football", last_name="Lopez"),
		"players_futbol": Player.objects.filter(curr_team__league__sport="Football"),
		"teams_sophia": Team.objects.filter(curr_players__first_name="Sophia"),
		"leagues_sophia": League.objects.filter(teams__curr_players__first_name="Sophia"),
		"players_flores_no": Player.objects.filter(last_name="Flores").exclude(curr_team__team_name= "Roughriders", curr_team__location= "Washington"),
		"teams_samuel": Team.objects.filter(all_players__first_name="Samuel", all_players__last_name="Evans"),
		"players_gatos": Player.objects.filter(all_teams__team_name="Tiger-Cats", all_teams__location="Manitoba"),
		"players_wichita_old": Player.objects.filter(all_teams__team_name="Vikings", all_teams__location="Wichita").exclude(curr_team__team_name="Vikings", curr_team__location="Wichita"),
		"team_gray": Team.objects.filter(all_players__first_name="Jacob", all_players__last_name="Gray").exclude(team_name="Colts", location="Oregon"),
		"players_joshua_no": Player.objects.filter(all_teams__league__name="Atlantic Federation of Amateur Baseball Players", first_name="Joshua"),
		"teams_12": Team.objects.annotate(numero_jugadores=Count('all_players')).filter(numero_jugadores__gte=12),
		"players_all": Player.objects.annotate(numero_teams=Count('all_teams')).order_by('-numero_teams')
		
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")